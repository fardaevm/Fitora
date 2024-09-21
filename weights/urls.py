from django.urls import path
from .views import WeightDetail, WeightListCreate

urlpatterns = [
    path("<int:pk>/", WeightDetail.as_view(), name="weight-detail"),
    path("", WeightListCreate.as_view(), name="weight-list"),
]