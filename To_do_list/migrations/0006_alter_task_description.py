# Generated by Django 3.2.7 on 2023-06-28 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_do_list', '0005_auto_20230628_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=1000, null=True, verbose_name='Описание'),
        ),
    ]