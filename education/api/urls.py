from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CuratorAPI, DirectionTrainingAPI, AcademicDisciplineAPI, StudyGroupAPI, StudentAPI, \
    DirectionTrainingXLSX, StudentXLSX, CuratorXLSX


urlpatterns =[
    path('curator/', CuratorAPI.as_view()),
    path('direction_training/', DirectionTrainingAPI.as_view()),
    path('academic_discipline/', AcademicDisciplineAPI.as_view()),
    path('study_group/', StudyGroupAPI.as_view()),
    path('student/', StudentAPI.as_view()),
    path('report_direction/', DirectionTrainingXLSX.as_view(), name='report_direction'),
    path('report_student/', StudentXLSX.as_view(), name='report_student'),
    path('report_curator/', CuratorXLSX.as_view(), name='report_curator'),
]