from rest_framework.response import Response
from rest_framework import generics, status
from university.models import Curator, DirectionTraining, AcademicDiscipline, StudyGroup, Student
from .serializers import CuratorSerializer, DirectionTrainingSerializer, AcademicDisciplineSerializer, \
    StudyGroupSerializer, StudentSerializer
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer


class CuratorAPI(generics.ListAPIView):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer

    def post(self, request):
        serializer = CuratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введены данные'}, status=status.HTTP_400_BAD_REQUEST)


class DirectionTrainingAPI(generics.ListAPIView):
    queryset = DirectionTraining.objects.all()
    serializer_class = DirectionTrainingSerializer

    def post(self, request):
        serializer = DirectionTrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введены данные'}, status=status.HTTP_400_BAD_REQUEST)


class AcademicDisciplineAPI(generics.ListAPIView):
    queryset = AcademicDiscipline.objects.all()
    serializer_class = AcademicDisciplineSerializer

    def post(self, request):
        serializer = AcademicDisciplineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введены данные'}, status=status.HTTP_400_BAD_REQUEST)


class StudyGroupAPI(generics.ListAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer

    def post(self, request):
        serializer = StudyGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введены данные'}, status=status.HTTP_400_BAD_REQUEST)


class StudentAPI(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введены данные'}, status=status.HTTP_400_BAD_REQUEST)


class DirectionTrainingXLSX(XLSXFileMixin, generics.ListAPIView):
    queryset = DirectionTraining.objects.all()
    serializer_class = DirectionTrainingSerializer
    renderer_classes = (XLSXRenderer,)
    filename = 'direction_training.xlsx'


class StudentXLSX(XLSXFileMixin, generics.ListAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    renderer_classes = (XLSXRenderer,)
    filename = 'student.xlsx'


class CuratorXLSX(XLSXFileMixin, generics.ListAPIView):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    renderer_classes = (XLSXRenderer,)
    filename = 'curator.xlsx'