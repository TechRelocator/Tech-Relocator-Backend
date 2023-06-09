# Generated by Django 4.2.1 on 2023-05-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_data', '0005_alter_job_education_alter_job_employment_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='education',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='employment_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='industry',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_function',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='job',
            name='senority',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
