from django.urls import path
from core.views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('users', UserViewSet, 'users')


urlpatterns = router.urls