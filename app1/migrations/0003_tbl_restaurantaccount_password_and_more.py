# Generated by Django 4.1.7 on 2023-05-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_fooditem_offer_tbl_feedback_tbl_foodmenu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_restaurantaccount',
            name='password',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_restaurantaccount',
            name='username',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]