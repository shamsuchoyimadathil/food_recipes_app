# Generated by Django 3.2.6 on 2021-09-04 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='ingredients',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='preparation',
            field=models.TextField(default=''),
        ),
    ]
