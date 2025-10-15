from django.urls import path

from doctors.apps import DoctorsConfig
from doctors.views import (CompanyView, ContactView, DoctorCreateView,
                           DoctorDeleteView, DoctorDetailView, DoctorListView,
                           DoctorUpdateView, HomeView, ProcessFormView)

app_name = DoctorsConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("company/", CompanyView.as_view(), name="company"),
    path("doctors/", DoctorListView.as_view(), name="doctor_list"),
    path("contacts/", ContactView.as_view(), name="contact"),
    path("doctors/create/", DoctorCreateView.as_view(), name="doctor_create"),
    path("doctors/<int:pk>/update/", DoctorUpdateView.as_view(), name="doctor_update"),
    path("doctors/<int:pk>/delete/", DoctorDeleteView.as_view(), name="doctor_delete"),
    path("doctors/<int:pk>/", DoctorDetailView.as_view(), name="doctor_detail"),
    path("post/", ProcessFormView.as_view(), name="process-form"),
]
