from typing import Any
from django.db import models

# Create your models here.

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

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class Authassignment(models.Model):
    itemname = models.CharField(primary_key=True, max_length=64)
    userid = models.CharField(max_length=64)
    bizrule = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authassignment'
        unique_together = (('itemname', 'userid'),)


class Authitem(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    type = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    bizrule = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authitem'


class Authitemchild(models.Model):
    parent = models.CharField(primary_key=True, max_length=64)
    child = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'authitemchild'
        unique_together = (('parent', 'child'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

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
    gestor = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='gestor')
    tipo = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupo'
        verbose_name='Grupo de trabajadores'
        verbose_name_plural='Grupos de trabajo'
        
    def __str__(self):
        return self.grupo


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
    id_oe = models.ForeignKey('ObjEstrategico', models.DO_NOTHING, db_column='id_oe')
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
    id_arc = models.ForeignKey(Arc, models.DO_NOTHING, db_column='id_arc')
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
    descripcion = models.CharField(max_length=250, blank=True, null=True)
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
    id_oe = models.ForeignKey(ObjEspecifico, models.DO_NOTHING, db_column='id_oe', blank=True, null=True)
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proyecto'


class ProyectoParticipante(models.Model):
    id_proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING, db_column='id_proyecto')
    id_participante = models.IntegerField()
    id_role = models.ForeignKey('RolProyecto', models.DO_NOTHING, db_column='id_role')

    class Meta:
        managed = False
        db_table = 'proyecto_participante'


class Rol(models.Model):
    rol = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol')
    permiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='permiso')

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
    id_tarea_pg = models.ForeignKey('TareaPrincipal', models.DO_NOTHING, db_column='id_tarea_pg', blank=True, null=True)
    creada_por = models.CharField(max_length=8)
    gestor = models.CharField(max_length=11, blank=True, null=True)
    id_proy = models.ForeignKey(Proyecto, models.DO_NOTHING, db_column='id_proy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea'
        verbose_name= 'Tarea'
        verbose_name_plural = 'Tareas'
    
    #para que aparezcan legible el nombre
    def __str__(self):
        return self.nombre
   

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
    id_tarea = models.ForeignKey(Tarea, models.DO_NOTHING, db_column='id_tarea')
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
        verbose_name= 'Tarea individual'
        verbose_name_plural = 'Tareas individuales'
        
    def __str__(self):
        return self.id_tarea.nombre

class TareaPgIndividual(models.Model):
    id_tarea_pg = models.ForeignKey('TareaPrincipal', models.DO_NOTHING, db_column='id_tarea_pg')
    id_trab = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarea_pg_individual'


class TareaPrincipal(models.Model):
    titulo = models.CharField(max_length=500)
    creada_por = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='creada_por')

    class Meta:
        managed = False
        db_table = 'tarea_principal'
        verbose_name= 'Tarea principal'
        verbose_name_plural = 'Tareas principales'
    
    def __str__(self):
        return self.titulo


class TareaPrincipalTrabajador(models.Model):
    id_tarea_principal = models.ForeignKey(TareaPrincipal, models.DO_NOTHING, db_column='id_tarea_principal')
    mes = models.IntegerField()
    anno = models.IntegerField()
    user_sap_code = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='user_sap_code')

    class Meta:
        managed = False
        db_table = 'tarea_principal_trabajador'


class Test(models.Model):
    id_tarea = models.IntegerField()
    cumplimiento = models.CharField(max_length=12)
    comentario = models.CharField(max_length=500, blank=True, null=True)
    modificada = models.IntegerField(blank=True, null=True)
    id_trab = models.CharField(max_length=8)
    responsable = models.CharField(max_length=255, blank=True, null=True)
    hora_inicio = models.CharField(max_length=10, blank=True, null=True)
    hora_fin = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateField()
    sede = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'test'


class TestNoslen(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'test_noslen'


class TrabGrupo(models.Model):
    id_grupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='id_grupo')
    sap_trab = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='sap_trab')

    class Meta:
        managed = False
        db_table = 'trab_grupo'


class TrabProyecto(models.Model):
    id_proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING, db_column='id_proyecto')
    id_area = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'trab_proyecto'


class Trazas(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.CharField(max_length=45)
    evento = models.CharField(max_length=45)
    resumen = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'trazas'


class Usuario(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=75)
    rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol')
    sap_code = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'usuario'