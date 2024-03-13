from django.urls import path
from . import views
from rest_framework import routers
from .api import MetaViewset

routers=routers.DefaultRouter()
routers.register('apiprueba',MetaViewset,'metaset')

urlpatterns = routers.urls

'''urlpatterns = [
    #path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('header/', views.header, name='encabezado'),
    path('listarIndicadores/', views.listarIndicadores, name='listarIndicadores'),

]'''
