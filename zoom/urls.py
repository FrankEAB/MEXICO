from django.urls import path
from .views import RegisterView, ProtectedView, UserDetailView, ProductListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected-view/', ProtectedView.as_view(), name='protected'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
