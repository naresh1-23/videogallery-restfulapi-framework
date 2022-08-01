
from django.forms import ValidationError
from rest_framework import serializers
from .models import Gallery
from moviepy.editor import VideoFileClip
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['caption', 'video', 'uploaded_at']

    def validate(self, validated_data):
        if validated_data.get('caption'):
            video = validated_data['video']
            file_size = video.size
            if file_size > 8e+6:
                raise ValidationError("max size is 1gb")
        return validated_data