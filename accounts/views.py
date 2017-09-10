import json
import logging

import requests
from django.conf import settings
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import permissions
from rest_framework import status
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from accounts import models as accounts_models
from accounts import serializers as accounts_serializers
from utils4geek.base.permissions import IsUserActive

logger = logging.getLogger(__name__)


# Create your views here.
def convert_to_dict(msg):
    return {'detail': msg}


class LoginAdminView(views.APIView):
    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            user_temp = accounts_models.User.objects.filter(username=username).first()
            if user_temp:
                if user_temp.is_active is False:
                    msg = _('Your account has been disabled.')
                    return Response(convert_to_dict(msg), status=403)

            if user:
                if not user.is_active:
                    msg = _('Your account has been disabled.')
                    return Response(convert_to_dict(msg), status=403)
                elif not user.is_staff:
                    msg = _('Unable to log in with provided credentials.')
                    raise ParseError(convert_to_dict(msg))
            else:
                msg = _('Unable to log in with provided credentials.')
                raise ParseError(convert_to_dict(msg))
        else:
            msg = _('Must include "username" and "password".')
            raise ParseError(convert_to_dict(msg))

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'user': {
                             "first_name": user.first_name,
                             "last_name": user.last_name,
                             "email": user.email,
                             "username": user.username,
                             "is_staff": user.is_staff,
                             "is_superuser": user.is_superuser,

                         }
                         }, status=status.HTTP_200_OK)


class SignUpFacebook(views.APIView):
    def post(self, request, format=None):

        # url para cambiar el code por un nuevo access_token
        access_token_url = 'https://graph.facebook.com/v2.8/oauth/access_token'

        # url para obtener datos de perfil
        graph_api_url = 'https://graph.facebook.com/v2.8/me?' \
                        'fields=id,last_name,first_name,email,hometown,picture.type(normal)'

        # obtener nuevo access_token
        redirect_uri = request.data.get('redirectUri', None)
        if redirect_uri is None:
            return Response(_("Missing 'redirectUri' in request"), status=status.HTTP_400_BAD_REQUEST)

        code = request.data.get('code')
        if code is None or code == "":
            return Response(_("Missing 'code' in request"), status=status.HTTP_400_BAD_REQUEST)

        params = {
            'client_id': settings.FACEBOOK_CLIENT,
            'redirect_uri': redirect_uri,
            'client_secret': settings.FACEBOOK_SECRET,
            'code': code
        }

        r = requests.get(access_token_url, params=params)
        try:
            access_token = json.loads(r.text)
        except Exception as e:
            return Response("error comunicationg with Facebook: %s" % str(e), status=status.HTTP_400_BAD_REQUEST)

        var_access_token = access_token.get("access_token", None)
        if var_access_token is None:
            return Response("error comunicationg with Facebook: %s" % str(r.text), status=status.HTTP_400_BAD_REQUEST)

        params = {
            'client_id': settings.FACEBOOK_CLIENT,
            'grant_type': "fb_exchange_token",
            'client_secret': settings.FACEBOOK_SECRET,
            'fb_exchange_token': var_access_token
        }

        # obtener datos de perfil
        r = requests.get(access_token_url, params=params)
        access_token = json.loads(r.text)

        r = requests.get(graph_api_url, params=access_token)

        profile = json.loads(r.text)

        user = accounts_models.User.objects.filter(facebook_id=profile["id"]).first()
        if user:
            if user.is_active == False:
                return Response(_("Your account has been disabled."), status=status.HTTP_403_FORBIDDEN)
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'registered': True,
                'token': token.key,
                'user': {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "facebook_picture_url": user.facebook_picture_url,
                    "hometown": user.hometown
                }
            }
            return Response(data, status=status.HTTP_200_OK)

        logger.info(profile)
        user = accounts_models.User()
        user.facebook_id = profile["id"]
        user.username = profile["id"]
        user.first_name = profile["first_name"]
        user.last_name = profile["last_name"]
        user.hometown = profile["hometown"]["name"] if "hometown" in profile.keys() else ""
        user.email = profile["email"] if 'email' in profile else str(profile['id'] + '@facebook.com')
        try:
            user.facebook_picture_url = profile['picture']['data']['url']
        except KeyError as e:
            logger.error("Error getting facebook profile picture from result: %s" % str(e))
        except Exception as e:
            logger.error("Error getting facebook profile picture: %s" % str(e))

        user.save()

        token, created = Token.objects.get_or_create(user=user)
        data = {
            'registered': True,
            'token': token.key,
            'user': {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "is_staff": user.is_staff,
                "facebook_picture_url": user.facebook_picture_url,
                "hometown": user.hometown
            }
        }
        return Response(data, status=status.HTTP_200_OK)


class SignUpFacebookMobile(views.APIView):
    def post(self, request, format=None):


        # url para obtener datos de perfil
        graph_api_url = 'https://graph.facebook.com/v2.8/me?' \
                        'fields=id,last_name,first_name,email,hometown,picture.type(normal)'

        # obtener nuevo access_token

        access_token = request.data.get('access_token')
        if access_token is None or access_token == "":
            return Response(_("Missing 'access_token' in request"), status=status.HTTP_400_BAD_REQUEST)

        data = {
            "access_token": access_token
        }
        r = requests.get(graph_api_url, params=data)

        if r.status_code != 200:
            return Response(r.text, status=status.HTTP_400_BAD_REQUEST)


        profile = json.loads(r.text)

        user = accounts_models.User.objects.filter(facebook_id=profile["id"]).first()

        if user:
            if user.is_active == False:
                return Response(_("Your account has been disabled"), status=status.HTTP_403_FORBIDDEN)

            token, created = Token.objects.get_or_create(user=user)
            data = {
                'registered': True,
                'token': token.key,
                'user': {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                    "facebook_picture_url": user.facebook_picture_url,
                    "hometown": user.hometown
                }
            }
            return Response(data, status=status.HTTP_200_OK)

        logger.info(profile)
        user = accounts_models.User()
        user.facebook_id = profile["id"]
        user.username = profile["id"]
        user.first_name = profile["first_name"]
        user.last_name = profile["last_name"]
        user.hometown = profile["hometown"]["name"] if "hometown" in profile.keys() else ""
        user.email = profile["email"] if 'email' in profile else str(profile['id'] + '@facebook.com')
        try:
            user.facebook_picture_url = profile['picture']['data']['url']
        except KeyError as e:
            logger.error("Error getting facebook profile picture from result: %s" % str(e))
        except Exception as e:
            logger.error("Error getting facebook profile picture: %s" % str(e))

        user.save()

        token, created = Token.objects.get_or_create(user=user)
        data = {
            'registered': True,
            'token': token.key,
            'user': {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "is_staff": user.is_staff,
                "facebook_picture_url": user.facebook_picture_url,
                "hometown": user.hometown
            }
        }
        return Response(data, status=status.HTTP_200_OK)

class LoginFacebook(views.APIView):
    def post(self, request, format=None):

        # url para cambiar el code por un nuevo access_token
        access_token_url = 'https://graph.facebook.com/v2.8/oauth/access_token'

        # url para obtener datos de perfil
        graph_api_url = 'https://graph.facebook.com/v2.8/me?' \
                        'fields=id,name,birthday,hometown,last_name,first_name,email, picture'

        # obtener nuevo access_token
        params = {
            'client_id': settings.FACEBOOK_CLIENT,
            'redirect_uri': "http://localhost:8000",
            'client_secret': settings.FACEBOOK_SECRET,
            'code': request.data.get('code')
        }

        r = requests.get(access_token_url, params=params)
        access_token = json.loads(r.text)
        var_access_token = access_token["access_token"]

        params = {
            'client_id': request.data.get('clientId'),
            'grant_type': "fb_exchange_token",
            'client_secret': settings.FACEBOOK_SECRET,
            'fb_exchange_token': var_access_token
        }

        # obtener datos de perfil
        r = requests.get(access_token_url, params=params)
        access_token = json.loads(r.text)

        r = requests.get(graph_api_url, params=access_token)

        profile = json.loads(r.text)

        user = accounts_models.User.objects.filter(facebook_id=profile["id"]).first()
        if user:
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'registered': True,
                'token': token.key
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'registered': False
            }

            return Response(data, status=status.HTTP_200_OK)




class ProfileView(views.APIView):
    serializer_class = accounts_serializers.ProfleSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserActive)


    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
