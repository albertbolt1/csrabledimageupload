# Generated by Django 3.2.4 on 2021-06-27 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientside', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantdiseaseimage',
            old_name='plantimage1',
            new_name='Image1',
        ),
        migrations.RenameField(
            model_name='plantdiseaseimage',
            old_name='plantimage2',
            new_name='Image2',
        ),
        migrations.RenameField(
            model_name='plantdiseaseimage',
            old_name='plantimage3',
            new_name='Image3',
        ),
    ]
