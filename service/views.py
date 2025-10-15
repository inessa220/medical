from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from service.models import Service


class ServiceListView(ListView):
    """Отображение списка всех доступных услуг."""

    model = Service
    template_name = "services_list.html"
    context_object_name = "services"


class ServiceCreateView(CreateView):
    """Создание новой услуги."""

    model = Service
    fields = (
        "name",
        "description",
        "price",
        "picture",
    )
    template_name = "service_form.html"

    def get_success_url(self):
        """Возвращает URL после успешного создания услуги."""
        return reverse_lazy("service:service_list")


class ServiceUpdateView(UpdateView):
    """Редактирование существующей услуги."""

    model = Service
    fields = (
        "name",
        "description",
        "price",
        "picture",
    )
    template_name = "service_form.html"

    def get_success_url(self):
        return reverse_lazy("service:service_list")


class ServiceDeleteView(DeleteView):
    """Удаление услуги с подтверждением действия."""

    model = Service
    template_name = "service_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("service:service_list")


class ServiceDetailView(DetailView):
    """Отображение деталей отдельной услуги."""

    model = Service
    template_name = "service_detail.html"
