from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'image']