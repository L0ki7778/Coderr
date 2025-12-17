from rest_framework.permissions import BasePermission, SAFE_METHODS

class ProfileOwner(BasePermission):
    def has_permission(self, request, view):
        
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        print(request.user.id, obj.id)
        if request.method in ['PATCH', 'PUT']:
            return request.user and request.user.id == obj.id
        if request.method != 'DELETE':
            return True
        return False