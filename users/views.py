from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from client.models import Record, Result
from users.forms import AccountEditForm, UserRegisterFrom
from users.models import User


class UserCreateView(CreateView):
    """Регистрация новых пользователей."""

    model = User
    form_class = UserRegisterFrom
    success_url = reverse_lazy("users:login")


class AccountView(DetailView):
    """Отображение аккаунта текущего пользователя."""

    model = User
    template_name = "account.html"
    context_object_name = "account"

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("users:account")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["records"] = Record.objects.filter(client=self.request.user)
        context["results"] = Result.objects.filter(client=self.request.user)
        return context


class EditProfileView(UpdateView):
    """Редактирование профиля пользователя."""

    model = User
    form_class = AccountEditForm
    template_name = "edit_profile.html"
    success_url = "account"

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("users:account")


class MyRecordsView(LoginRequiredMixin, ListView):
    """Отображение записей на прием текущего пользователя."""

    model = Record
    template_name = "users/my_records.html"
    context_object_name = "records"

    def get_queryset(self):
        return Record.objects.filter(client=self.request.user)


class UserResultView(LoginRequiredMixin, ListView):
    """Отображение результатов диагностики текущего пользователя."""

    model = Result
    template_name = "user_results.html"
    context_object_name = "results"

    def get_queryset(self):
        return Result.objects.filter(client=self.request.user)
