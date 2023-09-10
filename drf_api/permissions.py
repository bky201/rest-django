from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user
 from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
 
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
def your_protected_view(request):
    # Access the authenticated user
    user = request.user

    # Your view logic here
    if user.is_staff:
        return Response({"message": "This is a protected view for staff users."})
    else:
        return Response({"message": "This is a protected view for authenticated users."})