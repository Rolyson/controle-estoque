# Generated by Django 3.1.3 on 2023-10-11 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('sector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('quantity_served', models.FloatField(default=0)),
                ('is_consumable', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
            options={
                'verbose_name': 'Request_Product',
                'verbose_name_plural': 'Request_Products',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=1)),
                ('sector_in', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sector_in', to='sector.sector')),
                ('sector_out', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sector_out', to='sector.sector')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_movement', models.IntegerField(choices=[(1, 'In'), (2, 'Out')])),
                ('quantity', models.FloatField()),
                ('current', models.FloatField(blank=True, null=True)),
                ('previous', models.FloatField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.request')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sector.sector')),
            ],
            options={
                'verbose_name': 'Movement',
                'verbose_name_plural': 'Movements',
            },
        ),
    ]