# Generated by Django 4.2.6 on 2023-10-26 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department_mng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('date_of_joining', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('assigned_role', models.CharField(default='Employee', max_length=100)),
                ('current_project', models.CharField(default='None', max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('current_department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='department_mng.department')),
            ],
        ),
    ]
