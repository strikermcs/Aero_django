# Generated by Django 3.1a1 on 2020-06-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200615_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
    ]
