from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pagos',api.PagoViewSet,'pagos')
router.register(r'services',api.ServiceViewSet,'services')
router.register(r'expired_payments',api.ExpiredPaymentViewSet,'expiredPaymentens')
api_urlpatterns = router.urls