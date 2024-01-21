from django.urls import path
from .views import SectionCreateView, SectionDetailView, StudentCreateView, StudentDetailView


urlpatterns = [
    path('sections/', SectionCreateView.as_view(), name='section-list-create'),
    path('sections/<int:pk>', SectionDetailView.as_view(), name='section-detail'),
    path('sections/<int:section>/students', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>', StudentDetailView.as_view(), name='student-detail')    
]
