# Generated by Django 4.2.1 on 2023-06-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_queen_allstars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queen',
            name='allstars',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]