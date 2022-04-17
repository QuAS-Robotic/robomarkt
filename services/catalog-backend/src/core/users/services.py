

class UserService():
    def create_user(self, user_type, validated_data, *args, **kwargs):
        creation_func_name = "create_%s_user" % user_type
        getattr(self, creation_func_name)(validated_data, *args, **kwargs)
    
    def create_catalog_user(validated_data, *args, **kwargs):
        pass

    def create_admin_user(validated_data, *args, **kwargs):
        pass

    def create_analysis_user(validated_data, *args, **kwargs):
        pass