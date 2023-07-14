from django import forms
from django.core.exceptions import ValidationError
from .models import StudyGroup


class GroupsForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = ('__all__')

    """Метод для подсчёта колличества записей отошения многие ко многим"""
    def clean(self):
        student = self.cleaned_data.get('student')
        if student and student.count() > 20:
            raise ValidationError('Вгруппе не может быть больше 20 студентов')

        return self.cleaned_data