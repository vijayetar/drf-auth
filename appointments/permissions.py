from rest_framework import permissions

class IsApptUserOrReadOnly(permissions.BasePermission):
  def has_object_permission(self,request,view,obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.appt_user == request.user