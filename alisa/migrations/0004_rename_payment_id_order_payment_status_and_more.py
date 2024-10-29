# Generated by Django 5.0.4 on 2024-10-26 15:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alisa', '0003_alter_pickupstation_options_customeraddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment_id',
            new_name='payment_status',
        ),
        migrations.AddField(
            model_name='cart',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alisa.order')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alisa.product')),
            ],
            options={
                'verbose_name': 'orderitem',
                'verbose_name_plural': 'orderitems',
                'ordering': ['id'],
            },
        ),
    ]
