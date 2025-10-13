from django.test import TestCase
from django.urls import reverse

from doctors.models import Doctor


class HomeViewTest(TestCase):
    """Тестирование представления страницы home."""

    def test_home_view(self):
        response = self.client.get(reverse("doctors:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertIn("services", response.context)


class CompanyViewTest(TestCase):
    """Тестирование представления страницы company."""

    def test_company_view(self):
        response = self.client.get(reverse("doctors:company"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "company.html")
        self.assertIn("doctors", response.context)


class ContactViewTest(TestCase):
    """Тестирование представления страницы contact."""

    def test_contact_view(self):
        response = self.client.get(reverse("doctors:contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contacts.html")


class DoctorListViewTest(TestCase):
    """Тестирование представления списка врачей."""

    def setUp(self):
        Doctor.objects.create(first_name="test", last_name="test")

    def test_doctor_list_view(self):
        response = self.client.get(reverse("doctors:doctor_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "doctors_list.html")
        self.assertIn("doctors", response.context)
        self.assertEqual(len(response.context["doctors"]), 1)


class DoctorCreateViewTest(TestCase):
    """Тестирование создания врача."""

    def test_doctor_create_view(self):
        response = self.client.get(reverse("doctors:doctor_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "doctor_form.html")

    def test_doctor_create_post(self):
        data = {
            "first_name": "тест",
            "last_name": "тест",
            "patronymic": "тест",
            "education": "тест",
            "specialization": "тест",
            "experience": "тест",
        }
        response = self.client.post(reverse("doctors:doctor_create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Doctor.objects.count(), 1)


class DoctorUpdateViewTest(TestCase):
    """Тестирование редактирования врача."""

    def setUp(self):
        self.doctor = Doctor.objects.create(first_name="test", last_name="test")

    def test_doctor_update_view(self):
        response = self.client.get(
            reverse("doctors:doctor_update", args=[self.doctor.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "doctor_form.html")

    def test_doctor_update_post(self):
        data = {
            "first_name": "тест",
            "last_name": "тест",
            "patronymic": "тест",
            "education": "тест",
            "specialization": "тест",
            "experience": "тест",
        }
        response = self.client.post(
            reverse("doctors:doctor_update", args=[self.doctor.pk]), data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Doctor.objects.get(pk=self.doctor.pk).first_name, "тест")


class DoctorDeleteViewTest(TestCase):
    """Тестирование удаления врача."""

    def setUp(self):
        self.doctor = Doctor.objects.create(first_name="test", last_name="test")

    def test_doctor_delete_view(self):
        response = self.client.get(
            reverse("doctors:doctor_delete", args=[self.doctor.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "doctor_confirm_delete.html")

    def test_doctor_delete_post(self):
        response = self.client.post(
            reverse("doctors:doctor_delete", args=[self.doctor.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Doctor.objects.count(), 0)


class DoctorDetailViewTest(TestCase):
    """Тестирование возможности детального просмотра врача."""

    def setUp(self):
        self.doctor = Doctor.objects.create(first_name="test", last_name="test")

    def test_doctor_detail_view(self):
        response = self.client.get(
            reverse("doctors:doctor_detail", args=[self.doctor.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "doctor_detail.html")
        self.assertIn("doctor", response.context)


class ProcessFormViewTest(TestCase):
    """Тестирование отправки сообщения."""

    def test_process_form_view(self):
        data = {
            "name": "test",
            "email": "test@example.com",
            "message": "Test message",
        }
        response = self.client.post(reverse("doctors:process-form"), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Форма успешно отправлена!")
