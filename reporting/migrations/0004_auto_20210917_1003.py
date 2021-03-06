# Generated by Django 3.2.7 on 2021-09-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0003_batch_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='batch',
            name='batch_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
