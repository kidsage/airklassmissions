# Generated by Django 3.1.14 on 2022-09-24 21:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentshub', '0002_auto_20220925_0629'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Comment',
        ),
    ]
