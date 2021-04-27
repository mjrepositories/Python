# we are setting up permissions
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    # allowing users to edit their own profile

    def has_object_permission(self,request,view,obj):
    # checking if user is trying to edit their profile
        if request.method in permissions.SAFE_METHODS:
            return True

        # checking if user that is making a request is the use that is authorized
        return obj.id ==  request.user.id


# permission for updating items that belongs to a user
class UpdateOwnStatus(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        # check if the user is trying to update their own status
        if request.method in permissions.SAFE_METHODS:
            return True

        # if object has the same id as requesting user - it will return True
        return obj.user_profile.id == request.user.id