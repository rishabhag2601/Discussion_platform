# discussions/filters.py

import django_filters
from .models import Discussion, Hashtag

class DiscussionFilterSet(django_filters.FilterSet):
    hashtags = django_filters.ModelMultipleChoiceFilter(
        field_name='hashtags__name',
        to_field_name='name',
        queryset=Hashtag.objects.all()
    )

    class Meta:
        model = Discussion
        fields = {
            'text': ['icontains'],
        }
# discussions/filters.py

import django_filters
from .models import Hashtag

class HashtagFilterSet(django_filters.FilterSet):
    class Meta:
        model = Hashtag
        fields = ['name']
# discussions/filters.py

import django_filters
from .models import Comment

class CommentFilterSet(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = {
            'text': ['icontains'],
        }
