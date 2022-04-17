from django.urls import path, include, re_path
from core.api.routers import (
    CatalogRouter, HasuraRouter, 
    AnalysisRouter, PublicRouter, 
    UserRouter,
    )

"""
This section belongs to user urls. Only auth and user related urls should be included.
"""
from core.users.authentication.views import UserObtainTokenPairView, UserTokenRefreshView


user_router = UserRouter()
user_router.register(r'token/', UserObtainTokenPairView, basename='token_obtain_pair')
user_router.register(r'token/refresh/', UserTokenRefreshView, basename='token_refresh')

"""
This section belongs to catalog urls. Only catalog web site urls should be included.
"""

catalog_router = CatalogRouter()

"""
This section belongs to hasura urls
"""
from core.hasura.views import HasuraProxyView

hasura_router = HasuraRouter()

hasura_router.register('proxy', HasuraProxyView, basename='hasura_proxy')

'''
This section belongs to analysis urls.
'''
analysis_router = AnalysisRouter()

"""
This section belongs to public urls
"""
public_router = PublicRouter()
urlpatterns = [
    path('v1/catalog/', include(catalog_router.urls)),
    re_path('v1/hasura/proxy/(?P<source_path>.*)$', HasuraProxyView.as_view()),
    path('v1/analysis/', include(analysis_router.urls)),
    path('v1/public/', include(public_router.urls)),
    path("v1/user/token/", UserObtainTokenPairView.as_view(), name="token"),
    path("v1/user/token/refresh", UserTokenRefreshView.as_view(), name="token")
]

