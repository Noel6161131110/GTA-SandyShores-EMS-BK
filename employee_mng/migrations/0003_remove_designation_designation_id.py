# Generated by Django 4.2.6 on 2023-10-28 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_mng', '0002_designation_employee_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designation',
            name='designation_id',
        ),
    ]