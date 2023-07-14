from django.contrib import admin
from .models import Curator, DirectionTraining, AcademicDiscipline, StudyGroup, Student
from .forms import GroupsForm


class GroupsAdmin(admin.ModelAdmin):  # Класс для передачи формы с подчётом студентов в группе
    form = GroupsForm


admin.site.register(Curator)
admin.site.register(DirectionTraining)
admin.site.register(AcademicDiscipline)
admin.site.register(StudyGroup, GroupsAdmin)  # Регистрация формы с подсчётом студентов
admin.site.register(Student)