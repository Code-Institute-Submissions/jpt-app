# Generated by Django 3.0.3 on 2020-03-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(default='bookings_img/default.jpg', upload_to='bookings_img')),
                ('product_type', models.CharField(choices=[('class', 'Class'), ('item', 'Item')], max_length=30)),
            ],
        ),
    ]