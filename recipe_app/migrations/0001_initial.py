# Generated by Django 3.2.6 on 2021-08-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='food_images')),
                ('preparation_time', models.PositiveIntegerField()),
                ('ingredients', models.CharField(max_length=100)),
                ('preparation', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('native_food_of', models.CharField(blank=True, max_length=20)),
                ('cuisine_type', models.CharField(choices=[(1, 'Veg'), (2, 'Vegan'), (3, 'Eggetarian'), (4, 'Non Veg')], max_length=1)),
            ],
        ),
    ]