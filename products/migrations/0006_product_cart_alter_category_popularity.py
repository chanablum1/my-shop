# Generated by Django 5.1.1 on 2024-10-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('products', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart',
            field=models.ManyToManyField(related_name='products', to='cart.cart'),
        ),
        migrations.AlterField(
            model_name='category',
            name='popularity',
            field=models.IntegerField(),
        ),
    ]
