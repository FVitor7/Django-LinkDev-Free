from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Link
from django.contrib.auth.models import User


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('user', 'id', 'title', 'url',
                  'background_color', 'description', 'clicks_count', )
