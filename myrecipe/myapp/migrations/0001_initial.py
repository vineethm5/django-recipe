# Generated by Django 5.0.3 on 2024-03-07 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipename', models.CharField(max_length=100)),
                ('recipedescription', models.CharField(max_length=100)),
                ('recipeimg', models.ImageField(upload_to='recipeimg')),
            ],
        ),
    ]
