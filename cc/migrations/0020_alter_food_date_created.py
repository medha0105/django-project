# Generated by Django 3.2.4 on 2021-07-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0019_alter_food_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]