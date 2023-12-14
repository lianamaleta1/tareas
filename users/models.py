# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessControl(models.Model):
    ip = models.CharField(max_length=25)
    fecha = models.IntegerField()
    username = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'access_control'


class Area(models.Model):
    nombre = models.CharField(max_length=250)
    siglas = models.CharField(max_length=10)
    padre = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField()
    direccion = models.CharField(max_length=150, blank=True, null=True)
    centro_costo = models.CharField(max_length=20)
    id_uorg = models.IntegerField()
    sap_code = models.IntegerField()
    tipo_area = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'area'

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
    itemname = models.OneToOneField('Authitem', models.DO_NOTHING, db_column='name', primary_key=True)
    userid = models.OneToOneField('Usuario',models.DO_NOTHING,max_length=64)
    bizrule = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authassignment'

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
    parent = models.OneToOneField('Authitem', models.DO_NOTHING, db_column='parent', primary_key=True, related_name='parent_items')
    child = models.ForeignKey(Authitem, models.DO_NOTHING, db_column='child', related_name='child_items')

    class Meta:
        managed = False
        db_table = 'authitemchild'
        unique_together = (('parent', 'child'),)


class Capacitacion(models.Model):
    id_usuario = models.CharField(max_length=11)
    anno = models.IntegerField()
    mes = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=250)
    capacitador = models.CharField(max_length=150)
    categoria = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    region = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'capacitacion'


class Cargo(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    segmento = models.IntegerField()
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cargo'


class CentroEstudios(models.Model):
    id_usuario = models.CharField(max_length=11)
    nombre = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    desde = models.IntegerField()
    hasta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'centro_estudios'


class CentroLaboral(models.Model):
    id_usuario = models.CharField(max_length=11)
    departamento = models.CharField(max_length=150)
    direccion = models.CharField(max_length=100)
    entidad = models.CharField(max_length=150)
    organismo = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    desde = models.IntegerField()
    hasta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'centro_laboral'


class Competencias(models.Model):
    id_usuario = models.CharField(max_length=11)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'competencias'


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


class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'empresa'


class Eventos(models.Model):
    id_usuario = models.CharField(max_length=11)
    anno = models.IntegerField()
    nombre = models.CharField(max_length=150)
    entidad = models.CharField(max_length=150)
    organismo = models.CharField(max_length=150)
    lugar = models.CharField(max_length=150, blank=True, null=True)
    resultados = models.CharField(max_length=150, blank=True, null=True)
    comentarios = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventos'


class ExperienciaLaboral(models.Model):
    id_usuario = models.CharField(max_length=11)
    desde = models.IntegerField()
    hasta = models.IntegerField()
    nombre = models.CharField(max_length=150)
    comentario = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'experiencia_laboral'


class HisArea(models.Model):
    fecha_his = models.DateField()
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    padre = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField()
    direccion = models.CharField(max_length=150, blank=True, null=True)
    centro_costo = models.CharField(max_length=20)
    id_uorg = models.IntegerField()
    sap_code = models.IntegerField()
    tipo_area = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'his_area'


class HisCargo(models.Model):
    id_pk = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    segmento = models.IntegerField()
    estado = models.CharField(max_length=20)
    id = models.IntegerField()
    fecha_his = models.DateField()

    class Meta:
        managed = False
        db_table = 'his_cargo'


class HisExec(models.Model):
    fecha_exec = models.DateTimeField()
    status = models.CharField(max_length=150)
    cause = models.CharField(max_length=150)
    sap_trabajadores = models.IntegerField(blank=True, null=True)
    sap_estructura = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'his_exec'


class HisTrabajador(models.Model):
    fecha_his = models.DateField()
    ci = models.CharField(max_length=11)
    correo = models.CharField(max_length=100, blank=True, null=True)
    nombre_apellidos = models.CharField(max_length=250)
    genero = models.CharField(max_length=45)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    telef_casa = models.CharField(max_length=45, blank=True, null=True)
    telef_trabajo = models.CharField(max_length=45, blank=True, null=True)
    movil = models.CharField(max_length=45, blank=True, null=True)
    departamento = models.IntegerField()
    especialidad = models.CharField(max_length=45)
    escolaridad = models.CharField(max_length=45)
    grado = models.CharField(max_length=45)
    cargo = models.IntegerField()
    foto = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    titulo_trab = models.IntegerField()
    codigo = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'his_trabajador'


class HisUnidadOrganizativa(models.Model):
    idpk = models.AutoField(primary_key=True)
    fecha_his = models.DateField()
    id = models.IntegerField()
    uo_nombre = models.CharField(max_length=150)
    uo_siglas = models.CharField(max_length=10)
    uo_categoria = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'his_unidad_organizativa'


class Idiomas(models.Model):
    id_usuario = models.CharField(max_length=11)
    lengua = models.CharField(max_length=50)
    nivel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'idiomas'


class ImportarExcel(models.Model):
    codigo_indicador = models.CharField(max_length=255, blank=True, null=True)
    tiempo = models.CharField(max_length=255, blank=True, null=True)
    division = models.CharField(max_length=255, blank=True, null=True)
    uo_ct = models.CharField(max_length=255, blank=True, null=True)
    valor = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    fase = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'importar_excel'


class Noticia(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    autor = models.CharField(max_length=250)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'noticia'


class Permiso(models.Model):
    permiso = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=100)
    icono = models.CharField(max_length=150, blank=True, null=True)
    menu = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    padre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'permiso'


class Personal(models.Model):
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    ci = models.CharField(max_length=11)
    sexo = models.CharField(max_length=45)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    telef_casa = models.CharField(max_length=45, blank=True, null=True)
    movil = models.CharField(max_length=45, blank=True, null=True)
    foto = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField()
    fecha_nac = models.DateField()
    color_piel = models.CharField(max_length=20, blank=True, null=True)
    color_ojos = models.CharField(max_length=20, blank=True, null=True)
    estatura = models.CharField(max_length=10, blank=True, null=True)
    peso = models.CharField(max_length=10, blank=True, null=True)
    lugar_nac = models.CharField(max_length=100, blank=True, null=True)
    ciudadania = models.CharField(max_length=20, blank=True, null=True)
    estado_civil = models.CharField(max_length=10)
    nombre_conyugue = models.CharField(max_length=100, blank=True, null=True)
    ocupacion_conyugue = models.CharField(max_length=100, blank=True, null=True)
    nombre_padre = models.CharField(max_length=100, blank=True, null=True)
    ocupacion_padre = models.CharField(max_length=100, blank=True, null=True)
    direccion_padre = models.CharField(max_length=100, blank=True, null=True)
    nombre_madre = models.CharField(max_length=100, blank=True, null=True)
    ocupacion_madre = models.CharField(max_length=100, blank=True, null=True)
    direccion_madre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'


class Prueba(models.Model):
    nombre = models.CharField(max_length=255)
    descrip = models.CharField(max_length=1500)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'prueba'


class Reconocimientos(models.Model):
    id_usuario = models.CharField(max_length=11)
    anno = models.IntegerField()
    nombre = models.CharField(max_length=150)
    entidad = models.CharField(max_length=150, blank=True, null=True)
    organismo = models.CharField(max_length=150)
    lugar = models.CharField(max_length=150, blank=True, null=True)
    comentario = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconocimientos'


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


class SapEstructura(models.Model):
    id_area = models.CharField(primary_key=True, max_length=8)
    nombre_area = models.CharField(max_length=150)
    tipo_area = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sap_estructura'


class SapTrab(models.Model):
    area_code = models.CharField(max_length=100)
    personal_code = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=11)
    tipo_plaza = models.CharField(max_length=25)
    plaza = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sap_trab'


class Titulo(models.Model):
    titulo_nombre = models.CharField(max_length=100)
    titulo_descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'titulo'


class Trabajador(models.Model):
    ci = models.CharField(max_length=11)
    correo = models.CharField(max_length=100, blank=True, null=True)
    nombre_apellidos = models.CharField(max_length=250)
    genero = models.CharField(max_length=45)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    telef_casa = models.CharField(max_length=45, blank=True, null=True)
    telef_trabajo = models.CharField(max_length=45, blank=True, null=True)
    movil = models.CharField(max_length=45, blank=True, null=True)
    departamento = models.IntegerField()
    especialidad = models.CharField(max_length=45)
    escolaridad = models.CharField(max_length=45)
    grado = models.CharField(max_length=45)
    cargo = models.IntegerField()
    foto = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    titulo_trab = models.IntegerField()
    codigo = models.CharField(primary_key=True, max_length=11)

    class Meta:
        managed = False
        db_table = 'trabajador'


class Trazas(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.CharField(max_length=45)
    evento = models.CharField(max_length=45)
    resumen = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'trazas'


class UnidadOrganizativa(models.Model):
    uo_nombre = models.CharField(max_length=150)
    uo_siglas = models.CharField(max_length=10)
    uo_categoria = models.CharField(max_length=50)
    sap_code = models.IntegerField()
    direccion = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255)
    tipo_area = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'unidad_organizativa'


class Usuario(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol')
    grupo = models.IntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    area = models.IntegerField()
    cargo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'


class Viajes(models.Model):
    id_usuario = models.CharField(max_length=11)
    anno = models.IntegerField()
    pais = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'viajes'
