# Generated by Django 4.2.17 on 2024-12-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0002_rename_contenidoarticulo_articulowiki_contenido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulowiki',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='articulowiki',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='temawiki',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='temawiki',
            name='nombre',
        ),
        migrations.AddField(
            model_name='articulowiki',
            name='contenidoArticulo',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='articulowiki',
            name='tituloArticulo',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='temawiki',
            name='descripcionTema',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='temawiki',
            name='nombreTema',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
