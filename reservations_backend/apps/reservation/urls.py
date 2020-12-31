from django.urls import path

from reservations_backend.apps.reservation import views

urlpatterns = [
    path("", views.ReservationView.as_view()),
]
