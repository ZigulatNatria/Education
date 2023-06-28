from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CuratorAPI, DirectionTrainingAPI, AcademicDisciplineAPI, StudyGroupAPI, StudentAPI


urlpatterns =[
    path('curator/', CuratorAPI.as_view()),
    path('direction_training/', DirectionTrainingAPI.as_view()),
    path('academic_discipline/', AcademicDisciplineAPI.as_view()),
    path('study_group/', StudyGroupAPI.as_view()),
    path('student/', StudentAPI.as_view()),
]