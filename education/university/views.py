from django.shortcuts import render
from django.views.generic import ListView
from .models import DirectionTraining


class DirectionTrainingView(ListView):
    model = DirectionTraining
    template_name = 'index.html'
    context_object_name = 'direction_training'

