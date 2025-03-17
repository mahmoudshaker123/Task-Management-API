from django.urls import path
from .views import RegisterUserView, LoginView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'register': request.build_absolute_uri('register/'),
        'login': request.build_absolute_uri('login/'),
    })




urlpatterns = [
    
    path('', api_root, name='api-root'),

    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserDetailView.as_view(), name='user_detail'),
]
