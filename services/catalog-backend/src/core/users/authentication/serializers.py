import json
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['allowed_restricted_views'] = user.get_allowed_restricted_views_from_model()

        if "hasura_proxy" in token['allowed_restricted_views']:
            token["https://hasura.io/jwt/claims"] = {
                "x-hasura-allowed-roles": settings.HASURA_ALLOWED_ROLES,
                "x-hasura-default-role":  user.get_role(role_type="hasura")
            }

        return token
