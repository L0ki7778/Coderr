from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.accounts.models import User
from rest_framework.request import Request


class IsCustomer(BasePermission):
    def has_permission(self, request:Request, view):
        user:User=request.user
        if request.method in SAFE_METHODS:
            return True
        if request.method == "POST":
            return bool(user and user.type=="customer")
        return True
        
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' or request.method == 'PATCH':
            return bool(request.user and request.user.id == obj.reviewer.id)
        return True        
        
        
class isOrdererOrOfferer(BasePermission):
    def has_permission(self, request:Request, view):
        user:User=request.user
        if request.method == "POST":
            return bool(user and user.type=="customer")
        return True
    
    def has_object_permission(self, request, view, obj):
        if  request.method == 'PATCH':
            return bool(request.user and request.user.id == obj.business_user.id)
        if request.method == 'DELETE':
            return bool(request.user and (request.user.is_staff or request.user.is_superuser)) 
        
        
class IsOfferer(BasePermission):
    
    def has_permission(self, request, view):
        print(request.method)
        print(request.user.type)
        if request.method in SAFE_METHODS:
            print(f'triggered in safe methods')
            return True
        if request.method == 'POST':
            print(f'triggered {bool(request.user and request.user.type == 'business')}')
            return bool(request.user and request.user.type == 'business')
        return True
    
    def has_object_permission(self, request, view, obj):
        print(view,obj)
        if request.method == 'PATCH' or request.method == 'DELETE':
            return bool(request.user and request.user.id == obj.user.id)
        return True