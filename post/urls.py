from django.urls import path
from . import views

urlpatterns = [
    path("detail/<int:pk>/", views.PostDetailAPIView.as_view(), name="detail"),
]
