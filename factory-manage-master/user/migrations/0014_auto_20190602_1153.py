# Generated by Django 2.0 on 2019-06-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20190602_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='staff_type',
            field=models.CharField(max_length=100, verbose_name='职位'),
        ),
    ]
