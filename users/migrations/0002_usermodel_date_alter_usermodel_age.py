# Generated by Django 4.2.7 on 2023-11-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='age',
            field=models.BigIntegerField(),
        ),
    ]
