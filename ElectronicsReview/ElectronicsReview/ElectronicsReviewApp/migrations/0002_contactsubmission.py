# Generated by Django 5.0 on 2024-01-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElectronicsReviewApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('question', models.TextField()),
            ],
        ),
    ]