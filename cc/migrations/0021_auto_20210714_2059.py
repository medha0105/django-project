# Generated by Django 3.1.6 on 2021-07-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0020_alter_food_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]