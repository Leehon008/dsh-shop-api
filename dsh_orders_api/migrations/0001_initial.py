# Generated by Django 4.1.3 on 2022-11-05 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenue', models.CharField(db_index=True, max_length=200, verbose_name='revenue')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('quantity', models.PositiveIntegerField(verbose_name='stock')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Finished', 'Finished')], default='Active', max_length=12, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ['-created'],
            },
        ),
    ]
