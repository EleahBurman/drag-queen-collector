# Generated by Django 4.2.2 on 2023-06-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_performance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='date',
            field=models.DateField(verbose_name='Outfit date'),
        ),
    ]
