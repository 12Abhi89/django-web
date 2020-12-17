from django.urls import path
from . import views

labUrl = ''
# def getProject():
#     global labUrl
#     labUrl = 'projects/us011'

labUrl = r'projects/us011'
urlpatterns = [
    path('', views.home, name="home"),
    path(r'home',views.home, name="home"),
    path(r'projects',views.projects, name="projects"),
    path(labUrl,views.lab, name="lab")
]