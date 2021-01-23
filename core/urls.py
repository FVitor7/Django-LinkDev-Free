from django.urls import re_path
from .views import home_api, LinkViewSet
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash='optional')
router.register(r'links', LinkViewSet, basename='links')

urlpatterns = [
    re_path(r'^$', home_api),
]

urlpatterns += router.urls
