# Generated by Django 4.2.6 on 2023-10-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_mng', '0008_alter_employee_current_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='assigned_role',
            field=models.CharField(blank=True, default='Employee', max_length=100),
        ),
    ]
