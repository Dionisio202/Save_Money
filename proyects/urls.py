from rest_framework import routers
from .api import ProjectViewSet
router=routers.DefaultRouter()
router.register('api/proyects',ProjectViewSet,'proyects')
urlpatterns=router.urls