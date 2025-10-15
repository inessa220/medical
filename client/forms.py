from django import forms

from client.models import Result, Slot


class SlotForm(forms.ModelForm):
    """Форма для создания и редактирования слотов."""

    class Meta:
        model = Slot
        fields = ["start_time", "duration_minutes"]
        widgets = {
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "duration_minutes": forms.NumberInput(),
        }


class ResultForm(forms.ModelForm):
    """Форма для создания и редактирования результатов диагностики."""

    class Meta:
        model = Result
        fields = ["client", "doctor", "diagnosis", "recommendations", "comment"]
        widgets = {
            "client": forms.Select(attrs={"class": "form-select"}),
            "doctor": forms.Select(attrs={"class": "form-select"}),
            "diagnosis": forms.TextInput(attrs={"class": "form-control"}),
            "recommendations": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
        labels = {
            "client": "Пациент",
            "doctor": "Врач",
            "diagnosis": "Диагноз",
            "recommendations": "Рекомендации",
            "comment": "Комментарий",
        }
