# Generated by Django 4.0.6 on 2022-07-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='El titulo del libro', max_length=70)),
                ('fecha_publicacion', models.DateField(verbose_name='La fecha en el fue publicado el libro')),
                ('isbn', models.CharField(max_length=20, verbose_name='El ISBN del libro')),
            ],
        ),
    ]
