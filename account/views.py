# Create your views here.

from account.serializers import UserSerializer
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth import get_user_model


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [CustomUserPermission]
    queryset = get_user_model().objects.all()
