from rest_framework import serializers
from university.models import Curator, DirectionTraining, AcademicDiscipline, StudyGroup, Student


class StudentSerializer(serializers.ModelSerializer):
    # gender = Student.objects.filter(gender='Жен')

    class Meta:
        model = Student
        fields = [
            'name',
            'gender',
        ]


class StudyGroupSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)

    class Meta:
        model = StudyGroup
        fields = [
            'name',
            'student'
        ]


class AcademicDisciplineSerializer(serializers.ModelSerializer):
    study_group = StudyGroupSerializer(many=True)

    class Meta:
        model = AcademicDiscipline
        fields = [
            'name',
            'study_group',
        ]


class DirectionTrainingSerializer(serializers.ModelSerializer):
    academic_discipline = AcademicDisciplineSerializer(many=True)

    class Meta:
        model = DirectionTraining
        fields = [
            'name',
            'academic_discipline',
        ]


class CuratorSerializer(serializers.ModelSerializer):
    direction_training = DirectionTrainingSerializer(many=True)

    class Meta:
        model = Curator
        fields = '__all__'
