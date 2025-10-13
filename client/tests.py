from datetime import datetime

from django.test import TestCase
from django.utils.timezone import make_aware

from client.models import Record, Result, Slot
from doctors.models import Doctor
from users.models import User


class SlotModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doctor = Doctor.objects.create(first_name="test", last_name="test")

    def test_create_slot(self):
        """Проверяет создание слота"""
        slot = Slot.objects.create(
            doctor=self.doctor,
            start_time=make_aware(datetime(2025, 11, 10, 20, 0)),
            duration_minutes=20,
        )
        self.assertIsInstance(slot, Slot)
        self.assertEqual(str(slot), f"{self.doctor} {slot.start_time}")

    def test_unique_constraint(self):
        """Проверяет ограничение уникальности врача и времени старта"""
        first_slot = Slot.objects.create(
            doctor=self.doctor,
            start_time=make_aware(datetime(2025, 10, 15, 12, 10)),
            duration_minutes=10,
        )
        with self.assertRaises(Exception):
            Slot.objects.create(
                doctor=self.doctor,
                start_time=first_slot.start_time,
                duration_minutes=60,
            )


class RecordModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doctor = Doctor.objects.create(first_name="test", last_name="test")
        cls.slot = Slot.objects.create(
            doctor=cls.doctor,
            start_time=make_aware(datetime(2025, 10, 10, 15, 40)),
            duration_minutes=40,
        )
        cls.user = User.objects.create(
            email="patient@example.com", first_name="Patient", last_name="Example"
        )

    def test_create_record(self):
        """Проверяет создание записи на прием"""
        record = Record.objects.create(client=self.user, slot=self.slot)
        self.assertIsInstance(record, Record)
        self.assertIn(self.slot.id, Record.objects.values_list("slot_id", flat=True))

    def test_duplicate_booking(self):
        """Проверяет невозможность двойного бронирования одного слота"""
        Record.objects.create(client=self.user, slot=self.slot)
        with self.assertRaises(Exception):
            Record.objects.create(client=self.user, slot=self.slot)


class ResultModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doctor = Doctor.objects.create(first_name="test", last_name="test")
        cls.patient = User.objects.create(
            email="patient@example.com", first_name="Patient", last_name="Example"
        )

    def test_create_result(self):
        """Проверяет создание результата диагностики"""
        result = Result.objects.create(
            client=self.patient,
            doctor=self.doctor,
            diagnosis="Простуда",
            recommendations="Больше отдыхать",
        )
        self.assertIsInstance(result, Result)
        self.assertEqual(str(result), f"{self.patient} | Диагноз: Простуда...")
