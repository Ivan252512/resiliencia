# Generated by Django 2.1.7 on 2019-03-15 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ed_inundaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postedinundacion',
            name='youtube',
            field=models.BooleanField(default=False),
        ),
    ]
