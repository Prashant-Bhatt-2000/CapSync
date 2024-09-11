from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import UserSerializer, LoginSerializer
from .models import User

class CreateAccountView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'User registered successfully',
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'User registration failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



class VerifyEmail(APIView):
    def get(self, request, token):
        try:
            user = User.objects.get(verification_token=token)

            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({'message': 'Email successfully verified'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Email already verified'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)


class SigninVeiw(APIView):
    def post(self, request):
        data = request.data
        print(data)
        serializer = LoginSerializer(data=data)

        if serializer.is_valid():
            response_data = serializer.validated_data
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
