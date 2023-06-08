from django.urls import path
#Definiendo clases como vistas:
from .views import HomePageView, ResumePageView, ProjectsPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('resume/', ResumePageView.as_view(), name='resume'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('contact/', ContactPageView.as_view(), name='contact')
]