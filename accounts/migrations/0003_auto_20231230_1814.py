# Generated by Django 3.1 on 2023-12-30 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='last_name',
            new_name='lastname',
        ),
    ]