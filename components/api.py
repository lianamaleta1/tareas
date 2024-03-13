from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

class MetaViewset(viewsets.ModelViewSet):
 #we say query to do
  queryset=Meta.objects.all()
 #permissions
  permission_classes = [permissions.AllowAny] #or we can say IsAutenticate
  serializer_class= MetaSerializer
