# Generated by Django 4.2.6 on 2023-10-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_mng', '0006_remove_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='current_department',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='current_project',
            field=models.IntegerField(null=True),
        ),
    ]
