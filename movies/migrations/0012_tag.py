# Generated by Django 3.2.18 on 2023-04-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20230412_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]