# Generated by Django 3.1 on 2024-02-01 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20240201_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='blocked',
        ),
    ]
