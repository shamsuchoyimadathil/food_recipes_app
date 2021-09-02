# Generated by Django 3.2.6 on 2021-09-01 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0002_alter_recipes_cuisine_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.ManyToManyField(to='recipe_app.Ingredients'),
        ),
    ]