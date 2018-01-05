# Generated by Django 2.0 on 2017-12-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('judul', models.CharField(max_length=100)),
                ('tahun', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nama_genre', models.CharField(max_length=20)),
                ('ket', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='movie.Genre'),
        ),
    ]