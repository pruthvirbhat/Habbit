# Generated by Django 3.2.4 on 2021-06-20 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseWebapp', '0004_courses_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='name',
        ),
    ]
