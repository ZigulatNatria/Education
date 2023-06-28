# Generated by Django 4.2.2 on 2023-06-28 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Учебная дисциплина')),
            ],
            options={
                'verbose_name': 'Учебная дисциплина',
            },
        ),
        migrations.CreateModel(
            name='Curator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя куратора')),
            ],
            options={
                'verbose_name': 'Куратор',
            },
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Учебная группа')),
                ('academic_discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.academicdiscipline', verbose_name='Учебная дисциплина')),
            ],
            options={
                'verbose_name': 'Учебная группа',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя студента')),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.studygroup', verbose_name='Учебная группа')),
            ],
            options={
                'verbose_name': 'Студент',
            },
        ),
        migrations.CreateModel(
            name='DirectionTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Направление подготовки')),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.curator', verbose_name='Направление подготовки')),
            ],
            options={
                'verbose_name': 'Направление подготовки',
            },
        ),
        migrations.AddField(
            model_name='academicdiscipline',
            name='direction_training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.directiontraining', verbose_name='Направление подготовки'),
        ),
    ]
