# Generated by Django 2.1.7 on 2019-03-15 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_erupcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postrefvolcan',
            name='youtube',
            field=models.BooleanField(default=False),
        ),
    ]
