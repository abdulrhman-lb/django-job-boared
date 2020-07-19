# Generated by Django 3.0.6 on 2020-06-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_job_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('cover_letter', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Apply',
                'verbose_name_plural': 'Applys',
            },
        ),
    ]