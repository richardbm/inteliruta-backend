from rest_framework import views, permissions
from rest_framework.response import Response
from django.conf import settings

from utils4geek.base.renderers import PlainTextRenderer
import os
LOG_FILE_ABS_PATH = settings.LOG_FILE_ABS_PATH
PROJECT_ROOT = settings.PROJECT_ROOT
LOG_FILE_ABS_PATH = settings.LOG_FILE_ABS_PATH

# Create your views here.


class LogViewSet(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, _):
        log_file = open(LOG_FILE_ABS_PATH, 'r')
        text = log_file.read()
        log_file.close()
        return Response(text, status=200)


class LogFileViewSet(views.APIView):
    permission_classes = (permissions.IsAdminUser,)
    renderer_classes = (PlainTextRenderer,)

    def get(self, *args, **kwargs):
        filename = self.kwargs.get("filename")
        DIRNAME = os.path.join(PROJECT_ROOT, "logs")
        DIRNAME = os.path.join(DIRNAME, filename)
        log_file = open(DIRNAME, 'r')
        text = log_file.read()
        log_file.close()
        return Response(text, status=200)