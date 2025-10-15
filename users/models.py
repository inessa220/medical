from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель Пользователь."""

    username = None
    first_name = models.CharField(
        max_length=100, verbose_name="Имя", help_text="Введите имя"
    )
    last_name = models.CharField(
        max_length=100, verbose_name="Фамилия", help_text="Введите фамилию"
    )
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите email"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="телефонный номер",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Фото",
        blank=True,
        null=True,
        help_text="Добавьте фото профиля",
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город",
        blank=True,
        null=True,
        help_text="Введите город",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
