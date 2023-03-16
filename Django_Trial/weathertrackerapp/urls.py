from django.urls import path
from . import views
from weathertrackerapp.views import Index

#URL
urlpatterns = [
    path('', Index.as_view(), name='index'),
]