# Generated by Django 5.1.6 on 2025-02-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('req_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
