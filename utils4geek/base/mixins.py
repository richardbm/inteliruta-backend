"""
Basic building blocks for generic class based views.

We don't bind behaviour to http method handlers yet,
which allows mixin classes to be composed in interesting ways.
"""
from __future__ import unicode_literals

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.settings import api_settings
from utils4geek.base import pagination
from rest_framework.decorators import detail_route


class CreateModelMixin(object):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        validator = self.get_validator(data=request.data)
        if validator.is_valid(raise_exception=True):

            validator = self.pre_create(validator)
            instance = self.perform_create(validator)
            instance = self.post_create(instance)
            serializer = self.get_serializer(instance)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(validator.data, status=status.HTTP_400_BAD_REQUEST)

    def pre_create(self, validator):
        return validator

    def post_create(self, instance):
        return instance

    def perform_create(self, validator):
        if self.service_class:
            Service = self.service_class()
            instance = Service.create(validator.validated_data)
        else:
            model = self.get_model()
            instance = model(**validator.validated_data)
            instance.save()
        return instance

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}


class ListModelMixin(object):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveModelMixin(object):
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UpdateModelMixin(object):
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        validator = self.get_update_validator(instance, data=request.data, partial=partial)
        if validator.is_valid():
            validator.is_valid(raise_exception=True)
            validator = self.pre_update(instance, validator)
            instance = self.perform_update(validator)
            instance = self.post_update(instance)
            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)

    def pre_update(self, instance, validator):
        return validator

    def post_update(self, instance):
        return instance

    def perform_update(self, validator):
        if self.service_class:
            Service = self.service_class()
            instance = Service.update(validator.instance, validator.validated_data)
        else:
            data = validator.validated_data
            instance = self.get_object()
            for key, value in data.items():
                setattr(instance, key, value)
            instance.save()
        return instance

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DestroyModelMixin(object):
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.pre_delete(instance)
        self.perform_destroy(instance)
        self.post_delete(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def pre_delete(self, instance):
        return instance

    def post_delete(self, instance):
        return instance

    def perform_destroy(self, instance):
        instance.delete()

class DefaultPaginationMixin(object):
    pagination_class = pagination.DefaultLimitOffsetPagination

