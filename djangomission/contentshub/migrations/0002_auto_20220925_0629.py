# Generated by Django 3.1.14 on 2022-09-24 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentshub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klass',
            old_name='master',
            new_name='writer',
        ),
    ]
