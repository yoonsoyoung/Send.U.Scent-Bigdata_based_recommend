# Generated by Django 3.2.7 on 2021-09-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerfumeResult',
            fields=[
                ('perfume_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
            ],
        ),
    ]