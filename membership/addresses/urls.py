from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.Addresses.as_view()),
    path('<int:address_id>/', views.AddressDetail.as_view()),
    path('<int:address_id>/put/', views.PutAddress.as_view()),
    path('<int:address_id>/delete/', views.DeleteAddress.as_view()),
    path('getToken/', obtain_auth_token),
    ]