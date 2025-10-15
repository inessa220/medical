from django.contrib import admin

from client.models import Record, Slot


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "doctor",
        "start_time",
        "duration_minutes",
        "is_available",
    ]


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "client",
        "slot",
        "created_at",
    ]
