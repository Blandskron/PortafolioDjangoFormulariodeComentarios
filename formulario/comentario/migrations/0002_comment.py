# Generated by Django 5.0.4 on 2024-04-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]