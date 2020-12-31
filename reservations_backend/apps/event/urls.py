from django.urls import path

from reservations_backend.apps.event import views

urlpatterns = [
    path("", views.EventView.as_view()),
]
