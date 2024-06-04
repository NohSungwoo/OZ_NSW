from django.urls import path
from . import views

urlpatterns = [
    path('', views.Addresses.as_view()),
    path('<int:address_id>/put/', views.PutAddress.as_view()),
    path('<int:address_id>/delete/', views.DeleteAddress.as_view())
]