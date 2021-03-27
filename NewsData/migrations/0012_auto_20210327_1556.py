# Generated by Django 3.1.2 on 2021-03-27 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsData', '0011_auto_20210321_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsdata',
            name='hashVal',
        ),
        migrations.RemoveField(
            model_name='newsdata',
            name='user',
        ),
        migrations.AddField(
            model_name='newsdata',
            name='author',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='newsdata',
            name='category',
            field=models.CharField(default='general', max_length=20),
        ),
        migrations.AddField(
            model_name='newsdata',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='newsdata',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='newsdata',
            name='pub_date',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='newsdata',
            name='urlImage',
            field=models.TextField(null=True),
        ),
    ]