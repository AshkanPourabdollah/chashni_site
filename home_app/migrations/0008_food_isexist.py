# Generated by Django 4.2.4 on 2023-08-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0007_alter_food_foodimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='isExist',
            field=models.BooleanField(default=True),
        ),
    ]