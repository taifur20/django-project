# Generated by Django 2.0.10 on 2019-02-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='background_image',
            field=models.ImageField(default=0.0, help_text='For optimal quality, we recommend that you choose images that are at least 1600px wide', upload_to='product/%Y/%m/%d', verbose_name='background_image'),
            preserve_default=False,
        ),
    ]
