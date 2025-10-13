import os
from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse
from PIL import Image

from service.models import Service


def create_image_file():
    """Функция для создания фиктивного изображения."""

    img = Image.new("RGB", size=(100, 100))
    img_io = BytesIO()
    img.save(img_io, format="JPEG")
    img_file = SimpleUploadedFile(
        name="test.jpg", content=img_io.getvalue(), content_type="image/jpeg"
    )
    return img_file


class ServicesViewsTest(TestCase):
    """Класс для тестирования приложения service."""

    @classmethod
    def setUpTestData(cls):
        """Устанавливает общие данные для тестов."""

        cls.client = Client()
        cls.service = Service.objects.create(
            name="Тестовая услуга",
            description="Описание тестовой услуги.",
            price=1000,
            picture=None,
        )

    def test_service_list_view(self):
        """Тестирует просмотр списка услуг."""

        response = self.client.get(reverse("service:service_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "services_list.html")
        self.assertContains(response, "Тестовая услуга")

    def test_service_create_view(self):
        """Тестирует создание новой услуги."""

        data = {
            "name": "Новая услуга",
            "description": "Описание новой услуги.",
            "price": 1500,
            "picture": create_image_file() if os.getenv("TEST_WITH_IMAGE") else "",
        }
        response = self.client.post(reverse("service:service_create"), data=data)
        self.assertRedirects(response, reverse("service:service_list"))
        new_service = Service.objects.filter(name="Новая услуга").first()
        self.assertIsNotNone(new_service)

    def test_service_update_view(self):
        """Тестирует возможность обновления существующей услуги."""

        updated_data = {
            "name": "Обновленная услуга",
            "description": "Обновленное описание услуги.",
            "price": 2000,
            "picture": create_image_file() if os.getenv("TEST_WITH_IMAGE") else "",
        }
        response = self.client.post(
            reverse("service:service_update", args=[self.service.id]), data=updated_data
        )
        self.assertRedirects(response, reverse("service:service_list"))
        updated_service = Service.objects.get(id=self.service.id)
        self.assertEqual(updated_service.name, "Обновленная услуга")

    def test_service_delete_view(self):
        """Тестирует удаление услуги."""

        response = self.client.post(
            reverse("service:service_delete", args=[self.service.id])
        )
        self.assertRedirects(response, reverse("service:service_list"))
        deleted_service = Service.objects.filter(id=self.service.id).first()
        self.assertIsNone(deleted_service)

    def test_service_detail_view(self):
        """Тестирует просмотр детального отображение данных существующей услуги."""

        response = self.client.get(
            reverse("service:service_detail", args=[self.service.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "service_detail.html")
        self.assertContains(response, "Тестовая услуга")
