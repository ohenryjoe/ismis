# Generated by Django 3.2.7 on 2021-12-10 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='employees',
            name='designation_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hrms.designations'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='division_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hrms.divisions'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='salary_scale_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hrms.salaryscales'),
        ),
    ]
