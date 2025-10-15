from django.urls import path

from service.apps import ServiceConfig
from service.views import (ServiceCreateView, ServiceDeleteView,
                           ServiceDetailView, ServiceListView,
                           ServiceUpdateView)

app_name = ServiceConfig.name

urlpatterns = [
    path("services/", ServiceListView.as_view(), name="service_list"),
    path("services/create/", ServiceCreateView.as_view(), name="service_create"),
    path(
        "services/<int:pk>/update/", ServiceUpdateView.as_view(), name="service_update"
    ),
    path(
        "services/<int:pk>/delete/", ServiceDeleteView.as_view(), name="service_delete"
    ),
    path("services/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
]
