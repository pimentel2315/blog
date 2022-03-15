# Generated by Django 3.2 on 2022-03-10 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('decripcion', models.CharField(max_length=110, verbose_name='Descripcion')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('imagen', models.URLField(max_length=255)),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
