from rest_framework import serializers
from university.models import Curator, DirectionTraining, AcademicDiscipline, StudyGroup, Student


class CuratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curator
        fields = ('__all__')


class DirectionTrainingSerializer(serializers.ModelSerializer):
    curator = serializers.SlugRelatedField(slug_field='name', queryset=Curator.objects.all())

    class Meta:
        model = DirectionTraining
        fields = [
            'name',
            'curator',
        ]


class AcademicDisciplineSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcademicDiscipline
        fields = ('__all__')


class StudyGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudyGroup
        fields = ('__all__')


class StudentSerializer(serializers.ModelSerializer):
    study_group = serializers.SlugRelatedField(slug_field='name', queryset=StudyGroup.objects.all())

    class Meta:
        model = Student
        fields = ('__all__')