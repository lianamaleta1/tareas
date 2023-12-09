# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessControl(models.Model):
   
    ip = models.CharField(max_length=45)
    fecha = models.IntegerField()
    username = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'access_control'


class Arc(models.Model):
   
    ident = models.CharField(max_length=45)
    nombre = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'arc'


class Authassignment(models.Model):
    itemname = models.CharField(max_length=64, db_collation='utf8_general_ci')
    userid = models.CharField(max_length=64, db_collation='utf8_general_ci')
    bizrule = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    data = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authassignment'


class Authitem(models.Model):
    name = models.CharField(max_length=64, db_collation='utf8_general_ci')
    type = models.IntegerField()
    description = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    bizrule = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    data = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authitem'


class Authitemchild(models.Model):
    parent = models.CharField(max_length=64, db_collation='utf8_general_ci')
    child = models.CharField(max_length=64, db_collation='utf8_general_ci')

    class Meta:
        managed = False
        db_table = 'authitemchild'


class CategoriaDocumento(models.Model):
   
    categoria = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250)
    parent = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'categoria_documento'


class Documento(models.Model):
   
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    anno_pub = models.IntegerField()
    gestor_doc = models.CharField(max_length=100)
    fecha_sub = models.CharField(max_length=50)
    id_categoria = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'documento'


class Grupo(models.Model):
   
    grupo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    gestor = models.IntegerField()
    tipo = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupo'


class InfCump(models.Model):
   
    id_trab = models.IntegerField()
    mes = models.IntegerField()
    anno = models.IntegerField()
    inf_cualitativo = models.CharField(max_length=1000, blank=True, null=True)
    valoracion = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_cump'


class Noticia(models.Model):
   
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    autor = models.IntegerField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'noticia'


class ObjAnual(models.Model):
   
    ident = models.CharField(max_length=45)
    id_oe = models.IntegerField()
    nombre = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'obj_anual'


class ObjEspecifico(models.Model):
   
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'obj_especifico'


class ObjEstrategico(models.Model):
   
    ident = models.CharField(max_length=45)
    id_arc = models.IntegerField()
    nombre = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'obj_estrategico'


class Otra(models.Model):
   
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otra'


class Permiso(models.Model):
   
    permiso = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)
    url = models.CharField(max_length=100)
    icono = models.CharField(max_length=150, blank=True, null=True)
    menu = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    padre = models.CharField(max_length=50)
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permiso'


class Proyecto(models.Model):
   
    nombre_proyecto = models.CharField(max_length=250)
    siglas = models.CharField(max_length=10)
    cliente = models.CharField(max_length=150)
    alcance = models.CharField(max_length=25)
    responsable_des = models.CharField(max_length=100)
    responsable_ar = models.CharField(max_length=100)
    id_oe = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proyecto'


class ProyectoParticipante(models.Model):
   
    id_proyecto = models.IntegerField()
    id_participante = models.IntegerField()
    id_role = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proyecto_participante'


class Rol(models.Model):
   
    rol = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class RolPermiso(models.Model):
   
    rol = models.IntegerField()
    permiso = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rol_permiso'


class RolProyecto(models.Model):
   
    nombre_rol = models.CharField(max_length=150)
    descripcion_rol = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'rol_proyecto'


class Tarea(models.Model):
   
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)
    sede = models.CharField(max_length=100, blank=True, null=True)
    horario = models.CharField(max_length=50, blank=True, null=True)
    otro_horario = models.CharField(max_length=50, blank=True, null=True)
    contable = models.CharField(max_length=2, blank=True, null=True)
    extra = models.CharField(max_length=2)
    motivo = models.CharField(max_length=500, blank=True, null=True)
    id_tarea_pg = models.IntegerField(blank=True, null=True)
    creada_por = models.CharField(max_length=8)
    gestor = models.CharField(max_length=11, blank=True, null=True)
    id_proy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea'


class TareaColectiva(models.Model):
   
    id_tarea = models.IntegerField()
    id_tarea_asociada = models.IntegerField(blank=True, null=True)
    cumplimiento = models.IntegerField()
    comentario = models.CharField(max_length=500, blank=True, null=True)
    otros = models.CharField(max_length=255, blank=True, null=True)
    mostrar = models.CharField(max_length=255, blank=True, null=True)
    modificada = models.IntegerField(blank=True, null=True)
    id_area = models.IntegerField(blank=True, null=True)
    responsable = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea_colectiva'


class TareaDireccion(models.Model):
   
    id_tarea = models.IntegerField()
    cumplimiento = models.IntegerField()
    comentario = models.CharField(max_length=500, blank=True, null=True)
    otros = models.CharField(max_length=255, blank=True, null=True)
    mostrar = models.CharField(max_length=255, blank=True, null=True)
    modificada = models.IntegerField(blank=True, null=True)
    responsable = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea_direccion'


class TareaInd(models.Model):
   
    inicio = models.DateField()
    fin = models.DateField()
    asunto = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
    observaciones = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tarea_ind'


class TareaIndividual(models.Model):
   
    id_tarea = models.IntegerField()
    cumplimiento = models.CharField(max_length=12)
    comentario = models.CharField(max_length=2500, blank=True, null=True)
    modificada = models.IntegerField(blank=True, null=True)
    id_trab = models.CharField(max_length=8)
    responsable = models.CharField(max_length=255, blank=True, null=True)
    hora_inicio = models.CharField(max_length=10, blank=True, null=True)
    hora_fin = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateField()
    sede = models.CharField(max_length=100)
    justificacion = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea_individual'


class TareaPgIndividual(models.Model):
   
    id_tarea_pg = models.IntegerField()
    id_trab = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarea_pg_individual'


class TareaPrincipal(models.Model):
   
    titulo = models.CharField(max_length=500)
    creada_por = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarea_principal'


class TareaPrincipalTrabajador(models.Model):
   
    id_tarea_principal = models.IntegerField()
    mes = models.IntegerField()
    anno = models.IntegerField()
    user_sap_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarea_principal_trabajador'


class Test(models.Model):
   
    id_tarea = models.IntegerField()
    cumplimiento = models.CharField(max_length=12, db_collation='utf8_unicode_ci')
    comentario = models.CharField(max_length=500, db_collation='utf8_unicode_ci', blank=True, null=True)
    modificada = models.IntegerField(blank=True, null=True)
    id_trab = models.CharField(max_length=8, db_collation='utf8_unicode_ci')
    responsable = models.CharField(max_length=255, db_collation='utf8_unicode_ci', blank=True, null=True)
    hora_inicio = models.CharField(max_length=10, db_collation='utf8_unicode_ci', blank=True, null=True)
    hora_fin = models.CharField(max_length=10, db_collation='utf8_unicode_ci', blank=True, null=True)
    fecha = models.DateField()
    sede = models.CharField(max_length=100, db_collation='utf8_unicode_ci')

    class Meta:
        managed = False
        db_table = 'test'

class TrabGrupo(models.Model):
   
    id_grupo = models.IntegerField()
    sap_trab = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'trab_grupo'


class TrabProyecto(models.Model):
   
    id_proyecto = models.IntegerField()
    id_area = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'trab_proyecto'


class Trazas(models.Model):
   
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.CharField(max_length=45)
    evento = models.CharField(max_length=45)
    resumen = models.CharField(max_length=250, db_collation='utf8_unicode_ci')

    class Meta:
        managed = False
        db_table = 'trazas'
