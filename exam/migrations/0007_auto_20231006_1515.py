# Generated by Django 3.0.5 on 2023-10-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
