# Generated by Django 4.2.6 on 2023-10-28 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department_mng', '0002_remove_department_dep_id_remove_department_location_and_more'),
        ('org_projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='project_id',
        ),
        migrations.AddField(
            model_name='projects',
            name='dep_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='department_mng.department'),
        ),
    ]