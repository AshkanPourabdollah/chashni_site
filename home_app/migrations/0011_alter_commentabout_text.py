# Generated by Django 4.2.4 on 2023-09-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0010_alter_comments_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentabout',
            name='text',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
