# Generated by Django 4.1.2 on 2023-03-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared_models', '0002_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('specialization', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
