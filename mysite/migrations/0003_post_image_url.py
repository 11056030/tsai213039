# Generated by Django 4.2.6 on 2023-11-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_product_post_category_post_intro_post_isborrow_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(default='images/1.jpg', max_length=255),
        ),
    ]
