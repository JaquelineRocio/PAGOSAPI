from rest_framework.routers import DefaultRouter
from .api import ServiceViewSet
router=DefaultRouter()

router.register(r"services",ServiceViewSet,basename="services")


urlpatterns = router.urls