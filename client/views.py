from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  RedirectView, TemplateView, UpdateView)

from client.forms import ResultForm, SlotForm
from client.models import Record, Result, Slot


class AddSlotView(CreateView):
    """Создание слота приема врача."""

    model = Slot
    form_class = SlotForm
    template_name = "add_slot.html"

    def form_valid(self, form):
        try:
            form.instance.doctor_id = self.kwargs["doctor_pk"]
            response = super().form_valid(form)
            return response

        except IntegrityError:
            messages.error(self.request, "Такой слот уже существует и занят!")
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("client:slot_list", args=(self.kwargs["doctor_pk"],))


class SlotListView(ListView):
    """Список слотов врача."""

    model = Slot
    template_name = "slot_list.html"
    context_object_name = "slots"

    def get_queryset(self):
        doctor_pk = self.kwargs["doctor_pk"]
        queryset = Slot.objects.filter(doctor__pk=doctor_pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["doctor"] = {"pk": self.kwargs["doctor_pk"]}
        return context


class UpdateSlotView(UpdateView):
    """Обновление слота."""

    model = Slot
    form_class = SlotForm
    template_name = "update_slot.html"
    success_url = reverse_lazy("client:all_slots")


class DeleteSlotView(DeleteView):
    """Удаление слота."""

    model = Slot
    template_name = "slot_confirm_delete.html"
    success_url = reverse_lazy("client:all_slots")


class AllSlotsView(TemplateView):
    """Общий список всех слотов."""

    template_name = "all_slots.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slots"] = Slot.objects.all()
        return context


class FreeSlotsView(ListView):
    """Список свободных слотов."""

    model = Slot
    template_name = "free_slots.html"
    context_object_name = "free_slots"

    def get_queryset(self):
        occupied_slots = Record.objects.values_list("slot_id", flat=True)
        free_slots = Slot.objects.exclude(id__in=occupied_slots)
        return free_slots


class CreateRecordView(RedirectView):
    """Создание записи на прием пациента."""

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        slot_id = kwargs["slot_id"]
        current_user = self.request.user
        record = Record(client=current_user, slot_id=slot_id)
        record.save()
        return reverse("users:account")


class CreateResultView(CreateView):
    """Создание результата диагностики поциента."""

    model = Result
    form_class = ResultForm
    template_name = "result.html"
    success_message = "Запись успешно создана!"
    success_url = reverse_lazy("client:result_list")


class ResultListView(ListView):
    """Список результатов обследований."""

    model = Result
    template_name = "result_list.html"
    context_object_name = "results"


class ResultUpdateView(UpdateView):
    """Обновление результатов диагностики."""

    model = Result
    fields = (
        "client",
        "doctor",
        "diagnosis",
        "recommendations",
        "comment",
    )
    template_name = "result_form.html"

    def get_success_url(self):
        return reverse_lazy("client:result_list")


class ResultDeleteView(DeleteView):
    """Удаление результатов диагностики."""

    model = Result
    template_name = "result_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("client:result_list")


class ResultDetailView(DetailView):
    """Детальное отображение результата диагностики."""

    model = Result
    template_name = "result_detail.html"
