# Generated by Django 5.0 on 2023-12-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_rename_imaeg_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]