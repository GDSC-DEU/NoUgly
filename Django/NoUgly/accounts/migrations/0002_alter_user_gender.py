# Generated by Django 3.2.8 on 2022-03-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('여', '여자'), ('남', '남자')], max_length=20),
        ),
    ]
