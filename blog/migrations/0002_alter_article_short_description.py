# Generated by Django 4.2.2 on 2023-06-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short_description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
