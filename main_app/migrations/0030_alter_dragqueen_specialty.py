# Generated by Django 4.2.2 on 2023-06-09 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0029_alter_outfit_makeup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragqueen',
            name='specialty',
            field=models.CharField(default='comedy', max_length=250),
        ),
    ]
