# Generated by Django 4.0.4 on 2022-12-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVT_APP', '0007_remove_libro_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='portadas'),
        ),
    ]
