from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView
)
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Clientes', ClientesViews)

urlpatterns = [
    path('api/climatempo/token/', TokenObtainPairView.as_view()),
    path('api/climatempo/refresh/', TokenRefreshView.as_view()),
    path('api/climatempo/verify', TokenVerifyView.as_view()),
    path('api/climatempo/clientes/', include(router.urls))
]