# Generated by Django 3.0.5 on 2020-04-16 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tag',
            new_name='tags',
        ),
    ]