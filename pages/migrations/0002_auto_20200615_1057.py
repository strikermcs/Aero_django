# Generated by Django 3.1a1 on 2020-06-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_win',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
