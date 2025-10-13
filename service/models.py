from django.db import models


class Service(models.Model):
    """Модель Услуга."""

    name = models.CharField(max_length=100, verbose_name="Услуга")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    picture = models.ImageField(
        upload_to="services/picture",
        blank=True,
        default="img_7.png",
        verbose_name="Картинка",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["name"]
        permissions = [
            ("can_manage_services", "Может управлять услугами"),
        ]
