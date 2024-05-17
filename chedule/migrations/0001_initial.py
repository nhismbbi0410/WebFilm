# Generated by Django 5.0 on 2024-04-04 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_remove_category_tenfilm'),
        ('home', '0003_remove_film_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngaychieu', models.DateTimeField()),
                ('tenFilm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.film')),
                ('theloai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]