from django.urls import path
from rest_framework.routers import DefaultRouter

from post.views import PostViewSet, RateViewSet

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('rate', RateViewSet.as_view({'post': 'create', 'get': 'list'}), name='rate')
]
urlpatterns += router.urls
