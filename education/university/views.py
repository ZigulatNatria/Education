from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import DirectionTraining, Student, Curator, StudyGroup, AcademicDiscipline
import pandas as pd


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


def report(request):
    student = Student.objects.all()
    set_curator_direction_training = {curator: curator.directiontraining_set.all()
                                      for curator in Curator.objects.all().prefetch_related('directiontraining_set')}
    for key, value in set_curator_direction_training.items():

        print(key, value)
        print(len(value))

    print(set_curator_direction_training)

    # df = pd.DataFrame(
    #     set_curator_direction_training
    # )
    # df = pd.DataFrame({
    #     student,
    # })
    df = pd.DataFrame({'Name': ['Manchester City', 'Real Madrid', 'Liverpool',
                                'FC Bayern München', 'FC Barcelona', 'Juventus'],
                       'League': ['English Premier League (1)', 'Spain Primera Division (1)',
                                  'English Premier League (1)', 'German 1. Bundesliga (1)',
                                  'Spain Primera Division (1)', 'Italian Serie A (1)'],
                       'TransferBudget': [176000000, 188500000, 90000000,
                                          100000000, 180500000, 105000000]})


    df.to_excel('./teams.xlsx')
    return render(request, 'index.html')
