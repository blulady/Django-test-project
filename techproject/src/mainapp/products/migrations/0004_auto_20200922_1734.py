# Generated by Django 3.1.1 on 2020-09-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200921_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('treats', 'treats')], max_length=60),
        ),
    ]