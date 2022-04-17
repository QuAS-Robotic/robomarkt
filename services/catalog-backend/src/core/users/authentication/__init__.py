from rest_framework_simplejwt.authentication import JWTAuthentication

class ViewBasedJWTAuthentication(JWTAuthentication):

    def allowed_restricted_views(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return []

        validated_token = self.get_validated_token(raw_token)
        return validated_token.payload["allowed_restricted_views"]
