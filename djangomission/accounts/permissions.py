from rest_framework.permissions import BasePermission


#
class IsIndividualUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_individual)


class IsMasterUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_master)