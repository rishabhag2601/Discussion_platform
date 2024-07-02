from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        user = self.get_object()
        if user != request.user:
            request.user.following.add(user)
            return Response({'status': 'user followed'})
        return Response({'status': 'cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unfollow(self, request, pk=None):
        user = self.get_object()
        if user != request.user:
            request.user.following.remove(user)
            return Response({'status': 'user unfollowed'})
        return Response({'status': 'cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
