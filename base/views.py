from .pagination import DefaultPagination
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserList(ListCreateAPIView):

    permission_classes = [IsAdminUser]

    queryset = User.objects.all().exclude(is_superuser=True)

    serializer_class = UserSerializer

    pagination_class = DefaultPagination

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_admin'] = user.is_superuser

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




