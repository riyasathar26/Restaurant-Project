# Generated by Django 4.0.4 on 2023-05-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_satartdate_offer_startdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_useraccount',
            name='username',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]