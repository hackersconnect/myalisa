# Generated by Django 5.0.4 on 2024-10-13 09:41

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=250)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mode', models.CharField(default=None, max_length=50)),
                ('reference_code', models.CharField(default=None, max_length=100, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=250)),
                ('description', models.TextField(default=None, max_length=300)),
                ('current_price', models.FloatField(default=0.0)),
                ('previous_price', models.FloatField(default=0.0)),
                ('rating', models.IntegerField(default=0)),
                ('is_sold', models.BooleanField(default=False)),
                ('trending', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('flash', models.BooleanField(default=False)),
                ('added', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alisa.category')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('total_price', models.FloatField(default=0.0)),
                ('status', models.BooleanField(default=False)),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('payment_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alisa.payment')),
                ('product_link', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alisa.product')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('customer_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_link', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alisa.product')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default=None, max_length=13, null=True)),
                ('id_number', models.IntegerField(blank=True, default=0, null=True)),
                ('referee_email', models.EmailField(default=None, max_length=254, null=True)),
                ('shop_name', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(default=None, max_length=30, null=True)),
                ('is_set', models.BooleanField(default=False)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'ordering': ['user'],
            },
        ),
    ]
