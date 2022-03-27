# Generated by Django 4.0.3 on 2022-03-27 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='0', upload_to='images/')),
                ('category', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='photos.category')),
                ('location', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='photos.location')),
            ],
        ),
    ]
