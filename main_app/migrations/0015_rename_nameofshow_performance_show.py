# Generated by Django 4.2.1 on 2023-06-05 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_performance_nameofshow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performance',
            old_name='nameofshow',
            new_name='show',
        ),
    ]