# Generated by Django 4.1 on 2022-09-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_B_1', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
