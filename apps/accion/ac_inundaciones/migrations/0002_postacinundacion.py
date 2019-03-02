# Generated by Django 2.1.7 on 2019-03-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ac_inundaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAcInundacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitulo', models.CharField(blank=True, max_length=80, null=True)),
                ('parrafo', models.CharField(blank=True, max_length=800, null=True)),
                ('descripcionImagen', models.CharField(blank=True, max_length=200, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
        ),
    ]
