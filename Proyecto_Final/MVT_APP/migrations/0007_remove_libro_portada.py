# Generated by Django 4.0.4 on 2022-12-07 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MVT_APP', '0006_alter_libro_portada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='portada',
        ),
    ]
