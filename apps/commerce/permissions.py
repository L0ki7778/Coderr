from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import User
from rest_framework.request import Request


class IsCustomer(BasePermission):
    def has_object_permission(self, request:Request, view):
        user:User=request.user
        if request.method == "POST":
            return bool(user and user.type=="customer")
