# Generated by Django 3.0.5 on 2020-04-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0006_auto_20200411_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='authors',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='coevidence',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='cord_uid',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='doi',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='full_text_file',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='has_pdf_parse',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='has_pmc_xml_parse',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='journal',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='license',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='microsoft_pid',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pmcid',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='publish_time',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pubmed_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='sha',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='source_x',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='who',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
