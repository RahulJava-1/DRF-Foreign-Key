from django.shortcuts import render

from rest_framework import generics
from .models import Section, Student
from .serializers import SectionSerializer, StudentSerializer


# Create your views here.

class SectionCreateView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class StudentCreateView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        section = self.kwargs.get('section')
        return Student.objects.filter(section=section)
    
    def perform_create(self, serializer):
        section = self.kwargs.get('section')
        section = Section.objects.get(pk=section)
        serializer.save(section=section)

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer