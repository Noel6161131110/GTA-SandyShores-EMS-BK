# Generated by Django 4.2.6 on 2023-10-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designations', '0002_alter_designation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='name',
            field=models.CharField(default='employee', max_length=100, unique=True),
        ),
    ]
