# Generated by Django 3.2.5 on 2022-06-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Estado',
        ),
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
