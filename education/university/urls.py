from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import DirectionTrainingView, AcademicDisciplineView, StudentsView, report


urlpatterns =[
    path('', DirectionTrainingView.as_view(), name='first_page'),
    path('academic', AcademicDisciplineView.as_view(), name='academic'),
    path('student', StudentsView.as_view(), name='student'),
    path('report', report, name='report'),
]