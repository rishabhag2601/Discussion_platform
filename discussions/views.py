# discussions/views.py

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Discussion, Hashtag, Comment
from .filters import DiscussionFilterSet, HashtagFilterSet, CommentFilterSet
from .serializers import DiscussionSerializer, HashtagSerializer, CommentSerializer

class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DiscussionFilterSet

class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HashtagFilterSet

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilterSet
