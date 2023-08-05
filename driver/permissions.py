from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_object_permission(self, request, view):
        admin_permission = super().has_permission(request, view)
        return request.method == "GET" or admin_permission