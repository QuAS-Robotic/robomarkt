from rest_framework import HTTP_HEADER_ENCODING
from rest_framework_simplejwt.settings import api_settings
from rest_framework_proxy.views import ProxyView
from core.users.authentication.permissions import HasAccessToView


class AbstractProxyView(ProxyView):
    """Must implement the proxy_settings in the view you inherit from this class."""
    proxy_settings = None
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
        return "generic_proxy"