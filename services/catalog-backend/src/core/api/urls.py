from django.urls import path, include, re_path
from core.users.authentication.views import UserObtainTokenPairView, UserTokenRefreshView

user_urls = [
    path("v1/user/token/", UserObtainTokenPairView.as_view(), name="token"),
    path("v1/user/token/refresh", UserTokenRefreshView.as_view(), name="token"),
]

from core.hasura.views import  HasuraProxyView,  HasuraQueryView, HasuraMutationView

hasura_urls = [
    re_path('v1/hasura/proxy/(?P<source_path>.*)$', HasuraProxyView.as_view()),
    re_path('v1/hasura/query/(?P<source_path>.*)$', HasuraQueryView.as_view()),
    re_path('v1/hasura/mutation/(?P<source_path>.*)$', HasuraMutationView.as_view()),
]

analysis_urls = []

public_urls = []

urlpatterns = user_urls + hasura_urls + analysis_urls + public_urls

