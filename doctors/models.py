from django.db import models


class Doctor(models.Model):
    """Модель Доктор."""

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Отчество"
    )
    education = models.CharField(max_length=300, verbose_name="Образование")
    specialization = models.CharField(max_length=100, verbose_name="Специализация")
    experience = models.TextField(verbose_name="Опыт работы")
    avatar = models.ImageField(
        blank=True,
        upload_to="doctor/photo",
        default="img_6.png",
        verbose_name="Фото врача",
    )

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"
        ordering = ["last_name"]
        permissions = [
            ("can_manage_doctors", "Может управлять врачами"),
        ]

    def __str__(self):
        return (
            f"{self.last_name} {self.first_name} "
            f"{self.patronymic if self.patronymic else ''}, "
            f"{self.specialization}"
        )
