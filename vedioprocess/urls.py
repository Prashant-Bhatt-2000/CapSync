from django.urls import path
from .views import VedioUpload_View , GetSubtitles

urlpatterns = [
    path('vedioupload', VedioUpload_View.as_view(), name='upload_vedio'), 
    path('getsubtitles/<str:video>/', GetSubtitles.as_view(), name='get_subtitle'),
]