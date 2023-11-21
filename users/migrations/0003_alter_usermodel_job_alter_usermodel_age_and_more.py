# Generated by Django 4.2.7 on 2023-11-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_date_alter_usermodel_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='Job',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='age',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone_number',
            field=models.BigIntegerField(null=True),
        ),
    ]
