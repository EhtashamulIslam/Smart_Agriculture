# Generated by Django 4.2.6 on 2025-04-20 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FertilizerRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=50)),
                ('fertilizer_type', models.CharField(max_length=50)),
                ('amount_per_acre', models.FloatField(help_text='Amount in kg per acre')),
            ],
        ),
    ]
