# Generated by Django 4.1.2 on 2022-10-12 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roshitaappnew', '0003_delete_roshitamodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geeksmodel',
            name='last_modified',
        ),
    ]