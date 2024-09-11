from django.db import models
from uuid import uuid4
from accounts.models import User

class Video(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    video_thumbnail = models.FileField(upload_to='thumbnail/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, related_name='vedios', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subtitle(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    video = models.ForeignKey(Video, related_name='subtitles', on_delete=models.CASCADE)
    start_time = models.DurationField()
    end_time = models.DurationField()
    subtitle = models.TextField()

    def __str__(self):
        return f"{self.video.title} - {self.text[:30]}..."
