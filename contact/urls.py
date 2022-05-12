from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('message/', views.contact)
]

