from django.contrib import admin
from .models import Curator, DirectionTraining, AcademicDiscipline, StudyGroup, Student


admin.site.register(Curator)
admin.site.register(DirectionTraining)
admin.site.register(AcademicDiscipline)
admin.site.register(StudyGroup)
admin.site.register(Student)