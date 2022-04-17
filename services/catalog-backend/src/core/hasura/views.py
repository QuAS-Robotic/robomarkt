from re import I
from django.conf import settings
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework_simplejwt.settings import api_settings
from rest_framework_proxy.views import ProxyView
from rest_framework.permissions import IsAuthenticated
from core.users.authentication.permissions import HasAccessToView


class HasuraProxyView(ProxyView):
    proxy_settings = settings.HASURA_PROXY_SETTINGS
    source = "%(source_path)s"
    permission_classes = [HasAccessToView]

    def get_headers(self, request):
        headers = self.get_default_headers(request)
        token_header = request.META.get(api_settings.AUTH_HEADER_NAME)

        if isinstance(token_header, str):
            # Work around django test client oddness
            token_header = token_header.encode(HTTP_HEADER_ENCODING)

        headers["Authorization"] = token_header
        return headers

    def __str__(self) -> str:
        return "hasura_proxy"
