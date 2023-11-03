# Generated by Django 3.1.3 on 2023-11-03 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sector', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
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
            name='ProductRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('quantity_served', models.FloatField(default=0)),
                ('is_consumable', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.request')),
            ],
            options={
                'verbose_name': 'Product Request',
                'verbose_name_plural': 'Products Requests',
            },
        ),
        migrations.CreateModel(
            name='MovementProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_movement', models.IntegerField(choices=[(1, 'In'), (2, 'Out')])),
                ('quantity', models.FloatField()),
                ('current', models.FloatField(blank=True, null=True)),
                ('previous', models.FloatField(blank=True, null=True)),
                ('occurrence_data', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.request')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sector.sector')),
            ],
            options={
                'verbose_name': 'Movement Product',
                'verbose_name_plural': 'Movements Products',
            },
        ),
    ]
