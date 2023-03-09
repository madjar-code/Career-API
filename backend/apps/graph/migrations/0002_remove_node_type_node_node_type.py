# Generated by Django 4.1.7 on 2023-03-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='type',
        ),
        migrations.AddField(
            model_name='node',
            name='node_type',
            field=models.SmallIntegerField(choices=[(9, 'Edu'), (10, 'Job')], default=10),
        ),
    ]
