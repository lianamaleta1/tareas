from django.urls import path
from rest_framework import routers
from .api import MetaViewset
from .views import MetaAPIView
from components import views

routers=routers.DefaultRouter()
routers.register('apiprueba',MetaViewset,'metaset')

app_name = 'components'

urlpatterns = [
    #path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('header/', views.header, name='encabezado'),
    path('listarIndicadores/', views.listarIndicadores, name='listarIndicadores'),
    path('listadoMeta/<int:quantity>/',MetaAPIView.as_view(), name='listarmeta')

]
