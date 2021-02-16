from django.urls import path, include
from .views import DetailView

urlpatterns = [
    path('details/<int:id>',DetailView,name='details')
]
