# Generated by Django 3.1.2 on 2021-03-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsData', '0009_auto_20210321_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdata',
            name='hashVal',
            field=models.BigIntegerField(default=17),
        ),
    ]
