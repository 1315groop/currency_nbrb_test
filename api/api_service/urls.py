from config.views import ConfigViewSet
from config.views import RateViewSet
from config.views import UserRegistrationView
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


router = DefaultRouter()
router.register(r"config", ConfigViewSet)
router.register(r"rates", RateViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/user/register/", UserRegistrationView.as_view(), name="user_registration"
    ),
]
