# Generated by Django 3.1.2 on 2021-03-20 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsData', '0005_auto_20210321_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsdata',
            name='images',
        ),
    ]
