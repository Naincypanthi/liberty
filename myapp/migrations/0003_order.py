# Generated by Django 4.2.10 on 2024-03-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('phone_no', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('pay_mode', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
