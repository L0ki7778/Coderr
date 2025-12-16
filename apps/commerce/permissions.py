from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.accounts.models import User
from rest_framework.request import Request


class IsCustomer(BasePermission):
    def has_permission(self, request:Request, view):
        user:User=request.user
        if request.method == "POST":
            return bool(user and user.type=="customer")
        return True
        
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' or request.method == 'PATCH':
            return bool(request.user and request.user.id == obj.reviewer.id)
        return True        
        
        
