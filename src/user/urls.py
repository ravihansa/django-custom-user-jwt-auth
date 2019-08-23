from django.conf.urls import url
from rest_framework import routers
from .views import (UserRegisterView, UserLoginView, UserPasswordChangeView,
                    UserProfileview)

urlpatterns = [
    url(r"^register/$", UserRegisterView.as_view(), name="user-register"),
    url(r"^login/$", UserLoginView.as_view(), name="user-login"),
    url(r"^password-change/$", UserPasswordChangeView.as_view(),
        name="user-password-change"),
    url(r"^profile/$", UserProfileview.as_view(),
        name="user-profile"),
]
