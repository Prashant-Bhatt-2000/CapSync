from django.urls import path, include

urlpatterns =[
    path('accounts/', include('accounts.urls')),
    path('vedio/', include('vedioprocess.urls'))
]