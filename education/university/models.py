from django.core.exceptions import ValidationError
from django.db import models


class DbLimitException(BaseException):
    pass


class Curator(models.Model):
    name = models.CharField('Имя куратора', max_length=150)

    def __str__(self):
        return self.name


    """
    Тестовый метод ограничения колличества записей в таблице 
    P.S. оставлю на будущее вдруг где то пригодится :) 
    """
    # def save(self, *args, **kwargs):
    #     total_records = Curator.objects.count()
    #     if total_records >= 5:
    #         raise DbLimitException({"message": "Db limit reached please delete to add more data"})
    #     else:
    #         super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Куратор'


class DirectionTraining(models.Model):
    name = models.CharField('Направление подготовки', max_length=150)
    curator = models.ForeignKey(Curator, verbose_name='Куратор', on_delete=models.CASCADE,
                                related_name='direction_training')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление подготовки'


class AcademicDiscipline(models.Model):
    name = models.CharField('Учебная дисциплина', max_length=150)
    direction_training = models.ForeignKey(DirectionTraining, verbose_name='Направление подготовки',
                                           on_delete=models.CASCADE, related_name='academic_discipline')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учебная дисциплина'


class Student(models.Model):
    GENDER = [
        ('Муж', 'Муж'),
        ('Жен', 'Жен')
    ]

    name = models.CharField('Имя студента', max_length=150)
    gender = models.CharField('Пол', max_length=3, choices=GENDER, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'


class StudyGroup(models.Model):
    name = models.CharField('Учебная группа', max_length=150)
    academic_discipline = models.ForeignKey(AcademicDiscipline, verbose_name='Учебная дисциплина',
                                            on_delete=models.CASCADE, related_name='study_group')
    student = models.ManyToManyField(Student, verbose_name='Студенты', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учебная группа'
