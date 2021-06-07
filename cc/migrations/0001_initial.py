# Generated by Django 3.2.4 on 2021-06-07 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=100, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('height', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('category', models.CharField(choices=[('Active', 'Active'), ('Moderately active', 'Moderately active'), ('Inactive', 'Inactive')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100, null=True)),
                ('calorieAmount', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('carbAmount', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('proteinAmount', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('fatAmount', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('weightofItem', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('category', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snacks', 'Snacks')], max_length=40)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cc.customer')),
            ],
        ),
    ]
