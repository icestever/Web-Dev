# Generated by Django 4.1.7 on 2023-03-25 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-price'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
