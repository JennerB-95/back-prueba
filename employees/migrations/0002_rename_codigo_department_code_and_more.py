# Generated by Django 5.0.4 on 2024-04-30 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='codigo',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='codigo',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='codigo',
            new_name='code',
        ),
    ]
