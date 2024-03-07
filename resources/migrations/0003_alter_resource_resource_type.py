# Generated by Django 4.2.10 on 2024-03-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_resource_resource_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource_type',
            field=models.CharField(choices=[('videos', 'Videos'), ('podcasts', 'Posdcasts'), ('articles', 'Articles')], default='videos', max_length=50),
        ),
    ]
