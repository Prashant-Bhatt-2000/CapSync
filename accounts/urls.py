from django.urls import path
from .views import CreateAccountView, SigninVeiw, VerifyEmail

urlpatterns = [
    path('signup/', CreateAccountView.as_view(), name='create_account'),
    path('signin/', SigninVeiw.as_view(), name='signin'), 
    path("verifytoken/<str:token>/", VerifyEmail.as_view(), name='verify_email'),
]