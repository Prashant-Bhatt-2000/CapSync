from rest_framework import serializers
from uuid import uuid4
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from .email_verify import sendemail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        password = data.get('password')
        if password:
            data['password'] = make_password(password)

        email = data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists. Please login.')

        token = str(uuid4())
        data['verification_token'] = token

        sendemail(email, token)

        return data




from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import  RefreshToken

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError('Please enter "email" and "password".')

        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if user:
            if user.is_verified:
                refresh = RefreshToken.for_user(user)

                return {
                    'message': 'Login successful.',
                    'username': user.username,
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }
            else:
                raise serializers.ValidationError('You are not authorized to access this route.')
        else:
            raise serializers.ValidationError('Incorrect email or password.')
