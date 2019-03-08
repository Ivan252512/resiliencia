# Generated by Django 2.1.7 on 2019-03-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitulo', models.CharField(blank=True, max_length=80, null=True)),
                ('parrafo', models.CharField(blank=True, max_length=800, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='video/')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
        ),
    ]