# Generated by Django 2.1.7 on 2019-03-15 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_ladera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postrefladera',
            name='youtube',
            field=models.BooleanField(default=False),
        ),
    ]
