# Generated by Django 3.2.4 on 2021-06-20 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseWebapp', '0005_remove_courses_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='courseWebapp.category'),
        ),
    ]
