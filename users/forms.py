from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import BooleanField

from users.models import User


class StyleFormMixin:
    """Mixin-класс для автоматического добавления стилей ко всем элементам формы."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class UserRegisterFrom(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя."""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")


class AccountEditForm(UserChangeForm):
    """Форма редактирования пользователя."""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone", "city", "avatar")

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop("instance", None)
        super(AccountEditForm, self).__init__(instance=instance, *args, **kwargs)
        del self.fields["password"]
