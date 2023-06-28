from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import DirectionTraining, Student, Curator, StudyGroup, AcademicDiscipline


class DirectionTrainingView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        set_curator_direction_training = {curator: curator.directiontraining_set.all()
                                    for curator in Curator.objects.all().prefetch_related('directiontraining_set')}
        context['all_set_curator_direction_training'] = set_curator_direction_training
        return context


class AcademicDisciplineView(TemplateView):
    template_name = 'list_discipline.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        set_study_group = {academic_discipline: academic_discipline.studygroup_set.all()
                                    for academic_discipline in AcademicDiscipline.objects.all().prefetch_related('studygroup_set')}
        context['all_set_study_group'] = set_study_group
        return context


class StudentsView(TemplateView):
    template_name = 'list_student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        set_student = {study_group: study_group.student_set.all()
                       for study_group in StudyGroup.objects.all().prefetch_related('student_set')}
        context['all_set_student'] = set_student
        return context

