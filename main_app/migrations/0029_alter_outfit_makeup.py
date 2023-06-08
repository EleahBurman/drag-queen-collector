# Generated by Django 4.2.2 on 2023-06-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_alter_dragqueen_instagramhandle_alter_dragqueen_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='makeup',
            field=models.CharField(blank=True, choices=[('Mascara', 'Mascara'), ('Face Primer', 'Face Primer'), ('Foundation', 'Foundation'), ('Highlighter', 'Highlighter'), ('Glue Stick', 'Glue Stick'), ('Red Eye Shadow', 'Red Eye Shadow'), ('Orange Eye Shadow', 'Orange Eye Shadow'), ('Yellow Eye Shadow', 'Yellow Eye Shadow'), ('Green Eye Shadow', 'Green Eye Shadow'), ('Blue Eye Shadow', 'Blue Eye Shadow'), ('Purple Eye Shadow', 'Purple Eye Shadow'), ('Eyeliner', 'Eyeliner'), ('Translucent Powder', 'Translucent Powder'), ('False Lashes', 'False Lashes'), ('Lip Liner', 'Lip Liner'), ('Red Lipstick', 'Red Lipstick'), ('Pink Lipstick', 'Pink Lipstick'), ('Black Lipstick', 'Black Lipstick'), ('Clear Gloss', 'Clear Gloss'), ('Pink Gloss', 'Pink Gloss'), ('Red Gloss', 'Red Gloss'), ('Blush', 'Blush'), ('Bronzer', 'Bronzer')], default='Mascara', max_length=100, null=True),
        ),
    ]
