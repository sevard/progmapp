# Generated by Django 4.2 on 2023-08-06 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201223_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
