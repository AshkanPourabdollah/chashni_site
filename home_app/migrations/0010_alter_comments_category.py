# Generated by Django 4.2.4 on 2023-09-02 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0009_comments_category_comments_showing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home_app.food'),
        ),
    ]
