from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import DirectionTrainingView


urlpatterns =[
    path('', DirectionTrainingView.as_view(), name='first_page'),
]