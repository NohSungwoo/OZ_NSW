from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('', views.Addresses.as_view()),
    path('<int:address_id>/', views.AddressDetail.as_view()),
    path('<int:address_id>/put/', views.PutAddress.as_view()),
    path('<int:address_id>/delete/', views.DeleteAddress.as_view()),
    path('getToken/', obtain_auth_token),
    path('login/simpleJWT', TokenObtainPairView.as_view()),
    path('login/simpleJWT/refresh', TokenRefreshView.as_view()),
    path('login/simpleJWT/verify', TokenVerifyView.as_view())
    ]