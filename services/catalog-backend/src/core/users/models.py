from statistics import mode
from django.contrib import auth
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def get_allowed_restricted_views(self,request, *args, **kwargs):
        """
        get accessible views which requires access permission
        """
        allowed_restricted_views = list()
        for auth_backend in auth.get_backends():
            if hasattr(auth_backend, "allowed_restricted_views"):
                allowed_restricted_views += getattr(auth_backend, "allowed_restricted_views")(request)
        return allowed_restricted_views
    
    def get_allowed_restricted_views_from_model(self):
        qs = self.user_permissions.filter(codename="allowed_restricted_view").values_list("name", flat=True)
        return list(qs)

    def get_role(self, role_type:str):
        role_name_prefix = "{}__".format(role_type)
        try:
            role_obj = self.groups.get(name__startswith=role_name_prefix)
        except self.MultipleObjectsReturned:
            # TODO: ERROR HANDLING
            role_obj = self.groups.filter(name__startswith=role_name_prefix).first()
        
        return role_obj.name.split(role_name_prefix)[-1]