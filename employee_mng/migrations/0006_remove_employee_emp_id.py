# Generated by Django 4.2.6 on 2023-10-28 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_mng', '0005_alter_employee_current_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emp_id',
        ),
    ]
