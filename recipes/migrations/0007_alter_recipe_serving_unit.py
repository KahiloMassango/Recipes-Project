# Generated by Django 4.1.5 on 2023-01-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_category_alter_recipe_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='serving_unit',
            field=models.CharField(choices=[('PRATO/S', 'Pratos/s'), ('PESSOA/S', 'Pratos/s')], default='PLATES', max_length=10),
        ),
    ]
