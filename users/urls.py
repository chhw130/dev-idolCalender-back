from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),  # userList[ o ]
    path("admin", views.Admin.as_view()),  # adminProfile (pk:1)
    path("change-password", views.ChangePassword.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
    path("info/<int:pk>", views.UserDetail.as_view()),
    path("login", views.Login.as_view()),  # [ X ]
    path("logout", views.Logout.as_view()),  # [ X ]
    ###################
    # path("ME/schedules", views.MySchedule.as_view()),  # - 수현
    # --
]
