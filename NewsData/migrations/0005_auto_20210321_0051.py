# Generated by Django 3.1.2 on 2021-03-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsData', '0004_auto_20210321_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
