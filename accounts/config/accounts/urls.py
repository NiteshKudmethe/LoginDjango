from django.urls import path
from . import views
from .views import SignUpView

app_name = "accounts"

urlpatterns = [
    path("", views.homepage, name="homepage"),

    path("register", views.register_request, name="register"),
    path('signup/', SignUpView.as_view(), name='signup'),
]