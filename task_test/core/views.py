from core.models import  User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from core.serializers import  MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from core.serializers import UserRegistrationSerializer, UserSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

# Create your views here.
class UserViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    '''Вьюшка создания пользователя и получения списков пользователей'''
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    def get_serializer_class(self):
        if self.action == 'create':
           return UserRegistrationSerializer
        return UserSerializer
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer