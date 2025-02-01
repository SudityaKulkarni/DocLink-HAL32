from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from .import views
from .views import DoctorDetailView, DoctorRegisterView



urlpatterns = [
    path('api/doctor/list/', views.get_all_doctors, name="get-all-doctors"),
    path('api/admin/change-availibility/', views.change_availibity, name="change-availibility"),

    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctors/register-doctor/', DoctorRegisterView.as_view(), name='doctor-register'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

