# Generated by Django 5.0.3 on 2024-10-03 05:22

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
            name='FamilyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('looking_for', models.CharField(choices=[('My parents will stay with me after marriage', 'My parents will stay with me after marriage'), ('My parents will not stay with me after marriage', 'My parents will not stay with me after marriage'), ('Dont wish to specify', 'Dont wish to specify')], max_length=50)),
                ('family_values', models.CharField(max_length=100)),
                ('family_type', models.CharField(max_length=100)),
                ('family_status', models.CharField(max_length=100)),
                ('no_of_brothers', models.PositiveIntegerField()),
                ('no_of_brothers_married', models.PositiveIntegerField()),
                ('no_of_sisters', models.PositiveIntegerField()),
                ('no_of_sisters_married', models.PositiveIntegerField()),
                ('mother_tounge', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('mother_occupation', models.CharField(max_length=100)),
                ('family_wealth', models.CharField(max_length=100)),
                ('about_family', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='family_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]