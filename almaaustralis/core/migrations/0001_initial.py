# Generated by Django 3.2.5 on 2022-06-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('initial_class', models.CharField(blank=True, max_length=40, null=True)),
                ('info', models.CharField(blank=True, max_length=20, null=True)),
                ('url_image', models.URLField(verbose_name='URL image')),
            ],
            options={
                'verbose_name': 'Imagen Deslizante',
                'verbose_name_plural': 'Imagenes Deslizantes',
            },
        ),
        migrations.CreateModel(
            name='SocialNetworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('link', models.URLField(verbose_name='Link')),
                ('logo_class', models.CharField(max_length=15, verbose_name='Nombre logo')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
            },
        ),
        migrations.CreateModel(
            name='TextInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Titulo')),
                ('text', models.TextField(verbose_name='Texto')),
                ('url_image', models.URLField(verbose_name='URL image')),
            ],
            options={
                'verbose_name': 'Texto informativo',
                'verbose_name_plural': 'Textos informativos',
            },
        ),
    ]
