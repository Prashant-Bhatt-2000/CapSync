from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import VedioSerializer, SubtitleSerializer
from .models import Subtitle


class VedioUpload_View(APIView):
    authentication_classes = [JWTAuthentication]
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = VedioSerializer(data=data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response({'message': 'Video Uploaded successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class GetSubtitles(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, video):
        subtitles = Subtitle.objects.filter(video=video)
        if subtitles.exists():
            serializer = SubtitleSerializer(subtitles, many=True)  
            return Response({'message': 'Video subtitles found', 'subtitles': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No subtitles found for the given video'}, status=status.HTTP_404_NOT_FOUND)


