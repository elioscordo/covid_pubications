# Generated by Django 3.0.5 on 2020-04-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cord_uid', models.CharField(max_length=200)),
                ('sha', models.CharField(max_length=200)),
                ('source_x', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('doi', models.CharField(max_length=200)),
                ('pmcid', models.CharField(max_length=200)),
                ('pubmed_id', models.CharField(max_length=200)),
                ('license', models.CharField(max_length=200)),
                ('abstract', models.CharField(max_length=200)),
                ('publish_time', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('journal', models.CharField(max_length=200)),
                ('microsoft_pid', models.CharField(max_length=200)),
                ('who', models.CharField(max_length=200)),
            ],
        ),
    ]
