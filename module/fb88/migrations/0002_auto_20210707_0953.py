# Generated by Django 3.2.4 on 2021-07-07 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb88', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fb88',
            name='name',
            field=models.CharField(blank=True, help_text='Hay dien doi bong ban dat cuoc ', max_length=255, null=True, verbose_name='Dat cuoc cho doi bong than yeu'),
        ),
        migrations.AlterModelTable(
            name='image',
            table='fb88_image',
        ),
    ]
