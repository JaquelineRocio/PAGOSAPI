from . import api
from rest_framework import routers
from django.urls import path
from users.api import LoginView,RegisterView,GetUsers
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r'payments',api.PaymentsView,'payments')

payments_urlpatterns = router.urls

router_user = routers.DefaultRouter()
router_user.register(r'users',GetUsers,basename="read-only")

user_urlpatterns=[
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("create_jwt/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("refresh_jwt/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify_jwt/", TokenVerifyView.as_view(), name="token_verify"),
]


user_urlpatterns+=router_user.urls