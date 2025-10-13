from django.db import models

from doctors.models import Doctor
from users.models import User


class Slot(models.Model):
    """Модель Слот."""

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Доктор")
    start_time = models.DateTimeField(verbose_name="Дата")
    duration_minutes = models.PositiveIntegerField(
        default=30, verbose_name="Длительность"
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступность")

    def __str__(self):
        return f"{self.doctor} {self.start_time}"

    class Meta:
        verbose_name = "Слот"
        verbose_name_plural = "Слоты"

        constraints = [
            models.UniqueConstraint(
                fields=["doctor", "start_time"], name="unique_doctor_start_time"
            )
        ]


class Record(models.Model):
    """Модель Запись."""

    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент")
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE, verbose_name="Слот")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата записи")

    def __str__(self):
        return f"{self.client}! Вы записаны к {self.slot}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Result(models.Model):
    """Модель Результат диагностики."""

    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Доктор")
    diagnosis_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата постановки диагноза"
    )
    diagnosis = models.CharField(max_length=300, verbose_name="Диагноз")
    recommendations = models.TextField(verbose_name="Рекомендации")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.client} | Диагноз: {self.diagnosis[:50]}..."

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
