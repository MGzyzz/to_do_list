# Generated by Django 3.2.7 on 2023-06-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_do_list', '0003_auto_20230620_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=250, null=True, verbose_name='Имя'),
        ),
    ]