from rest_framework.permissions import BasePermission


class IsSelf(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit and retrieve it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id