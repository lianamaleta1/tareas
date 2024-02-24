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
    itemname = models.CharField(primary_key=True, max_length=64, db_collation='utf8_general_ci')  # The composite primary key (itemname, userid) found, that is not supported. The first column is selected.
    userid = models.CharField(max_length=64, db_collation='utf8_general_ci')
    bizrule = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    data = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authassignment'
        unique_together = (('itemname', 'userid'),)


class Authitem(models.Model):
    name = models.CharField(primary_key=True, max_length=64, db_collation='utf8_general_ci')
    type = models.IntegerField()
    description = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    bizrule = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    data = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authitem'


class Authitemchild(models.Model):
    parent = models.CharField(primary_key=True, max_length=64, db_collation='utf8_general_ci')  # The composite primary key (parent, child) found, that is not supported. The first column is selected.
    child = models.CharField(max_length=64, db_collation='utf8_general_ci')

    class Meta:
        managed = False
        db_table = 'authitemchild'
        unique_together = (('parent', 'child'),)


class Cargo(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    segmento = models.IntegerField()
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cargo'


class CategoriaDocumento(models.Model):
    categoria = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'categoria_documento'


class CategoriaIndicadores(models.Model):
    nombre_cat = models.CharField(max_length=100)
    descripcion_cat = models.CharField(max_length=100)
    estado_cat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categoria_indicadores'


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


class Documento(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    autor = models.CharField(max_length=250, blank=True, null=True)
    anno_pub = models.IntegerField(blank=True, null=True)
    gestor_doc = models.CharField(max_length=100)
    fecha_sub = models.DateField()
    hora_sub = models.TimeField()
    id_categoria = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'documento'


class Evento(models.Model):
    nombre = models.CharField(max_length=250)
    anno = models.IntegerField()
    lugar = models.CharField(max_length=250, blank=True, null=True)
    fecha_inicio = models.CharField(max_length=12, blank=True, null=True)
    fecha_fin = models.CharField(max_length=12, blank=True, null=True)
    modalidad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'evento'


class Galleta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=2500)
    codigo = models.IntegerField()
    id_usuario = models.ForeignKey(Documento, models.DO_NOTHING, db_column='id_usuario')
    monto = models.FloatField()

    class Meta:
        managed = False
        db_table = 'galleta'


class IndicadorValor(models.Model):
    id_indicador = models.IntegerField()
    valor = models.CharField(max_length=50)
    plan = models.CharField(max_length=50, blank=True, null=True)
    mes = models.IntegerField()
    anno = models.IntegerField()
    fecha_carga = models.DateField()
    nivel = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'indicador_valor'


class Meta(models.Model):
    orden = models.IntegerField()
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    tipo = models.CharField(max_length=100)
    comportamiento = models.CharField(max_length=50)
    um = models.CharField(max_length=100)
    formato = models.IntegerField()
    estado = models.IntegerField()
    formula = models.CharField(max_length=100, blank=True, null=True)
    icono = models.CharField(max_length=100)
    sec_cards = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meta'


class Mision(models.Model):
    nombre = models.CharField(max_length=2500)
    descripcion = models.CharField(max_length=2500)

    class Meta:
        managed = False
        db_table = 'mision'


class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=250)
    id_provincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='id_provincia')

    class Meta:
        managed = False
        db_table = 'municipio'


class Noticia(models.Model):
    titulo = models.CharField(max_length=1000)
    resumen = models.CharField(max_length=1000)
    contenido = models.CharField(max_length=5000)
    fecha_creacion = models.CharField(max_length=100)
    creado_por = models.CharField(max_length=100)
    foto = models.CharField(max_length=250, blank=True, null=True)
    publica = models.CharField(max_length=11, blank=True, null=True)
    carrusel = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noticia'


class Notificacion(models.Model):
    notif_descripcion = models.CharField(max_length=1500)
    notif_fecha = models.CharField(max_length=20)
    notif_estado = models.IntegerField()
    notif_url = models.CharField(max_length=250)
    notif_tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'notificacion'


class NotificacionUsuario(models.Model):
    id_usuario = models.IntegerField()
    id_notifcacion = models.ForeignKey(Notificacion, models.DO_NOTHING, db_column='id_notifcacion')
    fecha_vis = models.CharField(max_length=20)
    estado_vis = models.IntegerField()
    visto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion_usuario'


class Objetivo(models.Model):
    nombre = models.CharField(max_length=2500)
    descripcion = models.CharField(max_length=2500)
    anno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'objetivo'


class PaginaExcluida(models.Model):
    nombre_pagina = models.CharField(max_length=250)
    descripcion_pagina = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'pagina_excluida'


class Permiso(models.Model):
    permiso = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)
    url = models.CharField(max_length=100)
    icono = models.CharField(max_length=150, blank=True, null=True)
    menu = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    padre = models.CharField(max_length=50)
    visible = models.IntegerField()
    icono_tipo = models.CharField(max_length=20, blank=True, null=True)
    permiso_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permiso'


class Provincia(models.Model):
    nombre = models.CharField(max_length=250)
    siglas = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'provincia'


class Rol(models.Model):
    rol_nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)
    rol_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rol'


class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol')
    permiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='permiso')

    class Meta:
        managed = False
        db_table = 'rol_permiso'


class Trazas(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.CharField(max_length=45)
    evento = models.CharField(max_length=45)
    resumen = models.CharField(max_length=250, db_collation='utf8_unicode_ci')

    class Meta:
        managed = False
        db_table = 'trazas'


class UnidadMedida(models.Model):
    um_nombre = models.CharField(max_length=50)
    um_descripcion = models.CharField(max_length=250)
    um_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unidad_medida'


class Usuario(models.Model):
    username = models.CharField(max_length=255)
    rol = models.IntegerField()
    password = models.CharField(max_length=255)
    foto = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    sap_code = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'usuario'


class Valor(models.Model):
    nombre = models.CharField(max_length=1500)
    descripcion = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'valor'


class Vision(models.Model):
    nombre = models.CharField(max_length=2500)
    descripcion = models.CharField(max_length=2500)

    class Meta:
        managed = False
        db_table = 'vision'
