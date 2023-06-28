from django.core.exceptions import ValidationError
from django.db import models
from education import settings


class Curator(models.Model):
    name = models.CharField('Имя куратора', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Куратор'


class DirectionTraining(models.Model):
    name = models.CharField('Направление подготовки', max_length=150)
    curator = models.ForeignKey(Curator, verbose_name='Куратор', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление подготовки'


class AcademicDiscipline(models.Model):
    name = models.CharField('Учебная дисциплина', max_length=150)
    direction_training = models.ForeignKey(DirectionTraining, verbose_name='Направление подготовки',
                                           on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учебная дисциплина'


class StudyGroup(models.Model):
    name = models.CharField('Учебная группа', max_length=150)
    academic_discipline = models.ForeignKey(AcademicDiscipline, verbose_name='Учебная дисциплина',
                                            on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if StudyGroup.objects.count() < settings.MAX_STUDY_GROUP_COUNT:
    #         super().save(*args, **kwargs)
    #     raise ValidationError('Слишком много записей типа SomeModel!')

    class Meta:
        verbose_name = 'Учебная группа'


class Student(models.Model):
    name = models.CharField('Имя студента', max_length=150)
    study_group = models.ForeignKey(StudyGroup, verbose_name='Учебная группа', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
