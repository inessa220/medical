from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (AccountView, EditProfileView, MyRecordsView,
                         UserCreateView, UserResultView)

app_name = UsersConfig.name


urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("account/", AccountView.as_view(), name="account"),
    path("edit_profile/", EditProfileView.as_view(), name="edit_profile"),
    path("my-records/", MyRecordsView.as_view(), name="my_records"),
    path("my-diagnostics/", UserResultView.as_view(), name="user_results"),
]
