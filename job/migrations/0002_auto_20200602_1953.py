# Generated by Django 3.0.6 on 2020-06-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='JOBtitle',
            new_name='title',
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default=0, max_length=15, verbose_name=''),
            preserve_default=False,
        ),
    ]