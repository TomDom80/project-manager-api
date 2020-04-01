from rest_framework import permissions
import copy


class CustomDjangoModelPermission(permissions.DjangoModelPermissions):

    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)  # you need deepcopy when you inherit a dictionary type
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # if request.user.is_superuser:
        #     return True

        return obj.owner_ID == request.user