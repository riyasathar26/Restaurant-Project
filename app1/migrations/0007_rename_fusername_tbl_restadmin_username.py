# Generated by Django 4.1.7 on 2023-05-17 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_tbl_useraccount_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_restadmin',
            old_name='fusername',
            new_name='username',
        ),
    ]