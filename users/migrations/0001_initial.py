# Generated by Django 4.0 on 2023-12-26 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=25)),
                ('fecha', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'access_control',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('siglas', models.CharField(max_length=10)),
                ('padre', models.IntegerField(blank=True, null=True)),
                ('id_empresa', models.IntegerField()),
                ('direccion', models.CharField(blank=True, max_length=150, null=True)),
                ('centro_costo', models.CharField(max_length=20)),
                ('id_uorg', models.IntegerField()),
                ('sap_code', models.IntegerField()),
                ('tipo_area', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authitem',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('bizrule', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'authitem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=11)),
                ('anno', models.IntegerField()),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=250)),
                ('capacitador', models.CharField(max_length=150)),
                ('categoria', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'capacitacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('segmento', models.IntegerField()),
                ('estado', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CentroEstudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=11)),
                ('nombre', models.CharField(max_length=150)),
                ('titulo', models.CharField(max_length=150)),
                ('desde', models.IntegerField()),
                ('hasta', models.IntegerField()),
            ],
            options={
                'db_table': 'centro_estudios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CentroLaboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=11)),
                ('departamento', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=100)),
                ('entidad', models.CharField(max_length=150)),
                ('organismo', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('desde', models.IntegerField()),
                ('hasta', models.IntegerField()),
            ],
            options={
                'db_table': 'centro_laboral',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Competencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=11)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'competencias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('siglas', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=11)),
                ('anno', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('entidad', models.CharField(max_length=150)),
                ('organismo', models.CharField(max_length=150)),
                ('lugar', models.CharField(blank=True, max_length=150, null=True)),
                ('resultados', models.CharField(blank=True, max_length=150, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'eventos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExperienciaLaboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=11)),
                ('desde', models.IntegerField()),
                ('hasta', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('comentario', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'experiencia_laboral',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HisArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_his', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('siglas', models.CharField(max_length=10)),
                ('padre', models.IntegerField(blank=True, null=True)),
                ('id_empresa', models.IntegerField()),
                ('direccion', models.CharField(blank=True, max_length=150, null=True)),
                ('centro_costo', models.CharField(max_length=20)),
                ('id_uorg', models.IntegerField()),
                ('sap_code', models.IntegerField()),
                ('tipo_area', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'his_area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HisCargo',
            fields=[
                ('id_pk', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('segmento', models.IntegerField()),
                ('estado', models.CharField(max_length=20)),
                ('id', models.IntegerField()),
                ('fecha_his', models.DateField()),
            ],
            options={
                'db_table': 'his_cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HisExec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_exec', models.DateTimeField()),
                ('status', models.CharField(max_length=150)),
                ('cause', models.CharField(max_length=150)),
                ('sap_trabajadores', models.IntegerField(blank=True, null=True)),
                ('sap_estructura', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'his_exec',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HisTrabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_his', models.DateField()),
                ('ci', models.CharField(max_length=11)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_apellidos', models.CharField(max_length=250)),
                ('genero', models.CharField(max_length=45)),
                ('direccion', models.CharField(blank=True, max_length=250, null=True)),
                ('telef_casa', models.CharField(blank=True, max_length=45, null=True)),
                ('telef_trabajo', models.CharField(blank=True, max_length=45, null=True)),
                ('movil', models.CharField(blank=True, max_length=45, null=True)),
                ('departamento', models.IntegerField()),
                ('especialidad', models.CharField(max_length=45)),
                ('escolaridad', models.CharField(max_length=45)),
                ('grado', models.CharField(max_length=45)),
                ('cargo', models.IntegerField()),
                ('foto', models.CharField(blank=True, max_length=45, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('titulo_trab', models.IntegerField()),
                ('codigo', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'his_trabajador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HisUnidadOrganizativa',
            fields=[
                ('idpk', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_his', models.DateField()),
                ('id', models.IntegerField()),
                ('uo_nombre', models.CharField(max_length=150)),
                ('uo_siglas', models.CharField(max_length=10)),
                ('uo_categoria', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'his_unidad_organizativa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Idiomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=11)),
                ('lengua', models.CharField(max_length=50)),
                ('nivel', models.IntegerField()),
            ],
            options={
                'db_table': 'idiomas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImportarExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_indicador', models.CharField(blank=True, max_length=255, null=True)),
                ('tiempo', models.CharField(blank=True, max_length=255, null=True)),
                ('division', models.CharField(blank=True, max_length=255, null=True)),
                ('uo_ct', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('fase', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'importar_excel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=250)),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'db_table': 'noticia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permiso', models.CharField(max_length=250)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(max_length=100)),
                ('icono', models.CharField(blank=True, max_length=150, null=True)),
                ('menu', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('padre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'permiso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=11)),
                ('sexo', models.CharField(max_length=45)),
                ('direccion', models.CharField(blank=True, max_length=250, null=True)),
                ('telef_casa', models.CharField(blank=True, max_length=45, null=True)),
                ('movil', models.CharField(blank=True, max_length=45, null=True)),
                ('foto', models.CharField(blank=True, max_length=45, null=True)),
                ('edad', models.IntegerField()),
                ('fecha_nac', models.DateField()),
                ('color_piel', models.CharField(blank=True, max_length=20, null=True)),
                ('color_ojos', models.CharField(blank=True, max_length=20, null=True)),
                ('estatura', models.CharField(blank=True, max_length=10, null=True)),
                ('peso', models.CharField(blank=True, max_length=10, null=True)),
                ('lugar_nac', models.CharField(blank=True, max_length=100, null=True)),
                ('ciudadania', models.CharField(blank=True, max_length=20, null=True)),
                ('estado_civil', models.CharField(max_length=10)),
                ('nombre_conyugue', models.CharField(blank=True, max_length=100, null=True)),
                ('ocupacion_conyugue', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_padre', models.CharField(blank=True, max_length=100, null=True)),
                ('ocupacion_padre', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion_padre', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_madre', models.CharField(blank=True, max_length=100, null=True)),
                ('ocupacion_madre', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion_madre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'personal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descrip', models.CharField(max_length=1500)),
            ],
            options={
                'db_table': 'prueba',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reconocimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=11)),
                ('anno', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('entidad', models.CharField(blank=True, max_length=150, null=True)),
                ('organismo', models.CharField(max_length=150)),
                ('lugar', models.CharField(blank=True, max_length=150, null=True)),
                ('comentario', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'reconocimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RolPermiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'rol_permiso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SapEstructura',
            fields=[
                ('id_area', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(max_length=150)),
                ('tipo_area', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sap_estructura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SapTrab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code', models.CharField(max_length=100)),
                ('personal_code', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=100)),
                ('ci', models.CharField(max_length=11)),
                ('tipo_plaza', models.CharField(max_length=25)),
                ('plaza', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sap_trab',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_nombre', models.CharField(max_length=100)),
                ('titulo_descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'titulo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('ci', models.CharField(max_length=11)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_apellidos', models.CharField(max_length=250)),
                ('genero', models.CharField(max_length=45)),
                ('direccion', models.CharField(blank=True, max_length=250, null=True)),
                ('telef_casa', models.CharField(blank=True, max_length=45, null=True)),
                ('telef_trabajo', models.CharField(blank=True, max_length=45, null=True)),
                ('movil', models.CharField(blank=True, max_length=45, null=True)),
                ('departamento', models.IntegerField()),
                ('especialidad', models.CharField(max_length=45)),
                ('escolaridad', models.CharField(max_length=45)),
                ('grado', models.CharField(max_length=45)),
                ('cargo', models.IntegerField()),
                ('foto', models.CharField(blank=True, max_length=45, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('titulo_trab', models.IntegerField()),
                ('codigo', models.CharField(max_length=11, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'trabajador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trazas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('usuario', models.CharField(max_length=45)),
                ('evento', models.CharField(max_length=45)),
                ('resumen', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'trazas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadOrganizativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uo_nombre', models.CharField(max_length=150)),
                ('uo_siglas', models.CharField(max_length=10)),
                ('uo_categoria', models.CharField(max_length=50)),
                ('sap_code', models.IntegerField()),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('provincia', models.CharField(max_length=255)),
                ('tipo_area', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'unidad_organizativa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('grupo', models.IntegerField(blank=True, null=True)),
                ('fullname', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('area', models.IntegerField()),
                ('cargo', models.IntegerField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Viajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=11)),
                ('anno', models.IntegerField()),
                ('pais', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'viajes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authassignment',
            fields=[
                ('itemname', models.OneToOneField(db_column='name', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.authitem')),
                ('bizrule', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'authassignment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authitemchild',
            fields=[
                ('parent', models.OneToOneField(db_column='parent', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='parent_items', serialize=False, to='users.authitem')),
            ],
            options={
                'db_table': 'authitemchild',
                'managed': False,
            },
        ),
    ]
