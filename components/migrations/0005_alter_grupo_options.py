# Generated by Django 4.0 on 2023-12-26 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_alter_grupo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo',
            options={'managed': False, 'verbose_name': 'Grupo de trabajadores', 'verbose_name_plural': 'Grupos de trabajo'},
        ),
    ]