# Generated by Django 5.0.2 on 2024-04-18 12:19

import django.db.models.deletion
import store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_user', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('short_description', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('preview', models.ImageField(upload_to=store.models.generater_path)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(choices=[('Сахар', 'Сахар'), ('Фруктовые', 'Фруктовые'), ('Обычные', 'Обычные')], max_length=20)),
                ('popular', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.card')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.products')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField()),
                ('street', models.TextField()),
                ('home', models.TextField()),
                ('flot', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.card')),
                ('items', models.ManyToManyField(to='store.carditem')),
            ],
        ),
    ]
