# Generated by Django 2.1.7 on 2019-03-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postproyecto',
            name='descripcionImagen',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='postproyecto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='postproyecto',
            name='parrafo',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='postproyecto',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]