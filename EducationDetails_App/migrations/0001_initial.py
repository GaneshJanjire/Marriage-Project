# Generated by Django 5.1.1 on 2024-10-01 13:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('looking_for', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=100)),
                ('occupations', models.CharField(max_length=100)),
                ('occupation_details', models.TextField()),
                ('annual_income', models.CharField(max_length=20)),
                ('employed_in', models.CharField(max_length=50)),
                ('working_location', models.CharField(max_length=100)),
                ('special_cases', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='education_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]