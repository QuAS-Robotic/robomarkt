from django.conf import settings
from core.generics.views import AbstractProxyView
from core.hasura.validators import HasuraQueryValidator, HasuraMutationValidator

class HasuraProxyView(AbstractProxyView):
    proxy_settings = settings.HASURA_PROXY_SETTINGS
    source = "api/rest/%(source_path)s"
    http_method_names = ["get"]

    
    def __str__(self) -> str:
        return "hasura_proxy"


class HasuraQueryView(AbstractProxyView):
    proxy_settings = settings.HASURA_PROXY_SETTINGS
    source = "v1/graphql/%(source_path)s"
    http_method_names = ["post"]
    validator_class = HasuraQueryValidator

    def __str__(self) -> str:
        return "hasura_query"


class HasuraMutationView(AbstractProxyView):
    proxy_settings = settings.HASURA_PROXY_SETTINGS
    source = "v1/graphql/%(source_path)s"
    http_method_names = ["post"]
    validator_class = HasuraMutationValidator

    def __str__(self) -> str:
        return "hasura_mutation"
