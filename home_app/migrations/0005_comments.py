# Generated by Django 4.2.4 on 2023-08-21 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_food_category_alter_food_foodimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personName', models.CharField(default='', max_length=100)),
                ('commentText', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
