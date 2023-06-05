# Generated by Django 4.2.1 on 2023-06-05 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_outfit_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(default='Heart', max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
