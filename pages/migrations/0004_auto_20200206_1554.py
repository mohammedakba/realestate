# Generated by Django 3.0.2 on 2020-02-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200206_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadproperty',
            name='image1',
            field=models.ImageField(default='No Image', upload_to='pages/images'),
        ),
        migrations.AddField(
            model_name='uploadproperty',
            name='image2',
            field=models.ImageField(default='No Image', upload_to='pages/images'),
        ),
        migrations.AddField(
            model_name='uploadproperty',
            name='image3',
            field=models.ImageField(default='No Image', upload_to='pages/images'),
        ),
        migrations.AddField(
            model_name='uploadproperty',
            name='image4',
            field=models.ImageField(default='No Image', upload_to='pages/images'),
        ),
        migrations.AlterField(
            model_name='uploadproperty',
            name='image',
            field=models.ImageField(default='No Image', upload_to='pages/images'),
        ),
        migrations.AlterField(
            model_name='uploadproperty',
            name='property_type',
            field=models.CharField(choices=[('Sell', 'Sell'), ('Rent', 'Rent')], max_length=10),
        ),
    ]
