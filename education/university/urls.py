from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import index #DirectionTrainingView, AcademicDisciplineView, StudentsView


urlpatterns =[
    path('', index, name='first_page'),
    # path('', DirectionTrainingView.as_view(), name='first_page'),
    # path('academic', AcademicDisciplineView.as_view(), name='academic'),
    # path('student', StudentsView.as_view(), name='student'),
]