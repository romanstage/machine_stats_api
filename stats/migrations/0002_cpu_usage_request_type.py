# Generated by Django 3.2.4 on 2021-06-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu_usage',
            name='request_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
