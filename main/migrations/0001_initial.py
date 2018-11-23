# Generated by Django 2.1.3 on 2018-11-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('is_closed', models.BooleanField()),
                ('can_access_closed', models.BooleanField()),
                ('sex', models.IntegerField()),
                ('photo', models.CharField(max_length=100)),
                ('deactivated', models.CharField(blank=True, max_length=100, null=True)),
                ('university', models.IntegerField(blank=True, null=True)),
                ('university_name', models.CharField(blank=True, max_length=100, null=True)),
                ('faculty', models.IntegerField(blank=True, null=True)),
                ('faculty_name', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation', models.IntegerField(blank=True, null=True)),
                ('political', models.IntegerField(blank=True, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('inspired_by', models.CharField(blank=True, max_length=100, null=True)),
                ('people_main', models.IntegerField(blank=True, null=True)),
                ('life_main', models.IntegerField(blank=True, null=True)),
                ('smoking', models.IntegerField(blank=True, null=True)),
                ('alcohol', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]