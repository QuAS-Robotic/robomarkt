from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from .serializers import UserTokenObtainPairSerializer


class UserObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = UserTokenObtainPairSerializer

    def create(self, request, *args, **kwargs):
        return super(UserObtainTokenPairView).post(request, *args, **kwargs)

    @classmethod
    def get_extra_actions(cls):
        return []


class UserTokenRefreshView(TokenRefreshView):
    @classmethod
    def get_extra_actions(cls):
        return []

    def create(self, request, *args, **kwargs):
        return super(UserObtainTokenPairView).post(request, *args, **kwargs)