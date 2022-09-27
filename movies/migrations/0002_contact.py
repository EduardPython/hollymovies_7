# Generated by Django 4.0.4 on 2022-06-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=37)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('phone_number', models.IntegerField()),
                ('contact_at', models.DateField()),
            ],
        ),
    ]
