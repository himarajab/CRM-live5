# Generated by Django 3.0.2 on 2020-01-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200128_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('out for delivery', 'out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]