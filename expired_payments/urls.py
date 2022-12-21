from rest_framework.routers import DefaultRouter
from .api import ExpiredPaymentViewSet
router=DefaultRouter()

router.register(r"expired_payments",ExpiredPaymentViewSet,basename="expired_payments")

urlpatterns = router.urls