# Generated by Django 3.2.7 on 2021-12-14 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0008_auto_20211214_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='designation_id',
            new_name='designation',
        ),
    ]
