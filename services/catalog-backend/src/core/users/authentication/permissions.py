from rest_framework.permissions import IsAuthenticated

class HasAccessToView(IsAuthenticated):
    def has_permission(self, request, view):
        has_perm = super(HasAccessToView, self).has_permission(request, view)
        return has_perm and str(view) in request.user.get_allowed_restricted_views(request)
