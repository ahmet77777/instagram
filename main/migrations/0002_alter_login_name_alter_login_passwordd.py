# Generated by Django 4.1.5 on 2023-07-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='login',
            name='passwordd',
            field=models.CharField(max_length=1000),
        ),
    ]
