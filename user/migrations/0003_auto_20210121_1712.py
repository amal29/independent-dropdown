# Generated by Django 2.2.15 on 2021-01-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210121_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='coverpicture',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
