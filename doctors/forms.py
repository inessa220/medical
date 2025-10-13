from django import forms

from doctors.models import Doctor


class DoctorForm(forms.ModelForm):
    """Форма для создания и редактированния данных о врачах."""

    class Meta:
        model = Doctor
        fields = "__all__"
