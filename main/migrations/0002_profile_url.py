# Generated by Django 2.1.3 on 2018-11-23 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='url',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
