from rest_framework import serializers
from .models import Video, Subtitle
from .utils import extract_and_save_subtitles
import subprocess

class VedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'video_file', 'video_thumbnail']

    def validate(self, data): 
        title = data.get('title')
        video_file = data.get('video_file')
        video_thumbnail = data.get('video_thumbnail')

        if not title:
            raise serializers.ValidationError('Title is required.')
        
        if not video_thumbnail: 
            raise serializers.ValidationError('Video Thumbnail is required.')

        if video_file:
            file_name = video_file.name.lower()
            if not file_name.endswith(('.avi', '.mp4', '.mlt', '.webm')):
                raise serializers.ValidationError('Only .avi, .mp4, and .mlt files are allowed.')

        if video_thumbnail:
            file_name = video_thumbnail.name.lower()
            if not file_name.endswith(('.png', '.jpg')):
                raise serializers.ValidationError('Only .png and .jpg files are allowed.')

        return data

    def create(self, validated_data):
        video = Video.objects.create(**validated_data)

        extract_subtitle = extract_and_save_subtitles(video)
        print(extract_subtitle)

        return video


class SubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtitle
        fields = ['id', 'video', 'subtitle', 'start_time', 'end_time']
