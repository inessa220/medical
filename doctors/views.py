from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, TemplateView, UpdateView)

from doctors.models import Doctor
from service.models import Service
from users.models import User


class HomeView(TemplateView):
    """Домашняя страница."""

    template_name = "home.html"
    context_object_name = "home"

    def get_context_data(self, **kwargs):
        """Добавляет список услуг в контекст."""
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context


class CompanyView(TemplateView):
    """Страница о компании."""

    template_name = "company.html"
    context_object_name = "company"

    def get_context_data(self, **kwargs):
        """Добавляет список врачей в контекст."""
        context = super().get_context_data(**kwargs)
        context["doctors"] = Doctor.objects.all()
        return context


class ContactView(TemplateView):
    """Страница контактов."""

    template_name = "contacts.html"
    context_object_name = "contact"


class DoctorListView(ListView):
    """Список докторов с возможностью просмотра."""

    model = Doctor
    template_name = "doctors_list.html"
    context_object_name = "doctors"


class DoctorCreateView(CreateView):
    """Форма для добавления нового врача."""

    model = Doctor
    fields = (
        "first_name",
        "last_name",
        "patronymic",
        "education",
        "specialization",
        "experience",
        "avatar",
    )
    template_name = "doctor_form.html"

    def get_success_url(self):
        return reverse_lazy("doctors:doctor_list")


class DoctorUpdateView(UpdateView):
    """Форма для редактирования профиля доктора."""

    model = Doctor
    fields = (
        "first_name",
        "last_name",
        "patronymic",
        "education",
        "specialization",
        "experience",
        "avatar",
    )
    template_name = "doctor_form.html"

    def get_success_url(self):
        return reverse_lazy("doctors:doctor_list")


class DoctorDeleteView(DeleteView):
    """Удаление доктора из БД с подтверждением перед удалением."""

    model = Doctor
    template_name = "doctor_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["doctors"] = User.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy("doctors:doctor_list")


class DoctorDetailView(DetailView):
    """Подробная информация о конкретном враче."""

    model = Doctor
    template_name = "doctor_detail.html"


class ProcessFormView(FormView):
    """Представление для обработки формы обратной связи."""

    template_name = "process_form.html"
    success_url = "/"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Заявка с сайта от {name}"

        full_message = f"""
                Заявка с сайта:\n
                Имя: {name}\n
                Email: {email}\n
                Сообщение: {message}
                """

        sender_email = "inessasizyova@yandex.ru"
        recipient_email = "inessa220@mail.ru"

        email_message = EmailMessage(
            subject=subject,
            body=full_message,
            from_email=sender_email,
            to=[recipient_email],
        )
        email_message.send()

        return HttpResponse("Форма успешно отправлена!")
