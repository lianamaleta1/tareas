from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def header(request):
    cantNotificaciones= 'hola'
    sql_query = """
        SELECT COUNT(n.id)
        FROM notificacion n
        WHERE n.id NOT IN (
            SELECT nu.id_notifcacion
            FROM notificacion_usuario nu
            WHERE nu.id_usuario = %s
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(sql_query, [request.user.id])  # Assuming request is available in your context
        cant_notif = cursor.fetchone()[0]

    return render(request, "header.html",{'cant_notif':cant_notif})

#CRUD de INDICADORES:
def listarIndicadores(request):

    listado= Noticia.objects.all().order_by('-hora_creacion')
    hello='acabado sencillo'

    return render(request,'metas/listado.html',{'listado':listado,'hello':hello})


class MetaAPIView(APIView):

    def get(self,*args,**kwargs):

        quantity = int(self.kwargs["quantity"])#esto es para la paginacion
        meta=Meta.objects.filter(estado=1)[:quantity]
        serializer=MetaSerializer(meta,many =True)

        return Response(serializer.data)
