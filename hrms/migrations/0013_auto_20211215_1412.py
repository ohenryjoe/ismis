# Generated by Django 3.2.7 on 2021-12-15 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0012_auto_20211214_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designations',
            name='created_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='designations',
            name='headed_entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.entitylevel'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='marital_status',
            field=models.CharField(choices=[('M', 'Married'), ('S', 'Single'), ('W', 'Widowed'), ('D', 'Divorced')], default='Uganda', max_length=50),
        ),
        migrations.AlterField(
            model_name='employees',
            name='religion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hrms.religions'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mister'), ('Ms', 'Miss'), ('Mrs', 'Mrs'), ('Dr.', 'Doctor'), ('Eng.', 'Engineer'), ('Prof.', 'Professor'), ('Hon.', 'Honourable')], default='Mr', max_length=50),
        ),
    ]
