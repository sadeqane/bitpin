from django.db.models import Prefetch
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from post.models import Post, Rate
from post.permission import IsSelf
from post.serializers import PostSerializer, RateSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related(Prefetch("rate_set", queryset=Rate.objects.all()))
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsSelf]


class RateViewSet(CreateModelMixin,ListModelMixin,RetrieveModelMixin, GenericViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticated]
