from django.urls import path

from client.apps import ClientConfig
from client.views import (AddSlotView, AllSlotsView, CreateRecordView,
                          CreateResultView, DeleteSlotView, FreeSlotsView,
                          ResultDeleteView, ResultDetailView, ResultListView,
                          ResultUpdateView, SlotListView, UpdateSlotView)

app_name = ClientConfig.name


urlpatterns = [
    path("<int:doctor_pk>/slots/", SlotListView.as_view(), name="slot_list"),
    path("<int:doctor_pk>/add-slot/", AddSlotView.as_view(), name="add_slot"),
    path("all-slots/", AllSlotsView.as_view(), name="all_slots"),
    path("slots/edit/<int:pk>/", UpdateSlotView.as_view(), name="update_slot"),
    path("slots/delete/<int:pk>/", DeleteSlotView.as_view(), name="delete_slot"),
    path("free-slots/", FreeSlotsView.as_view(), name="free_slots"),
    path(
        "record/create/<int:slot_id>/", CreateRecordView.as_view(), name="create_record"
    ),
    path("create_result/", CreateResultView.as_view(), name="create-result"),
    path("result_list/", ResultListView.as_view(), name="result_list"),
    path("result/update/<int:pk>/", ResultUpdateView.as_view(), name="result_update"),
    path("result/delete/<int:pk>/", ResultDeleteView.as_view(), name="result_delete"),
    path("result/detail/<int:pk>/", ResultDetailView.as_view(), name="result_detail"),
]
