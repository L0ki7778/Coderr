from rest_framework.permissions import BasePermission

class ProfileOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "PATCH":
            return bool(request.user and request.user.id == obj.id)
        return False