from django.urls import path
from . import views

urlpatterns = [
    #path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('header/', views.header, name='encabezado'),
]
