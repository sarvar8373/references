# Generated by Django 5.0.6 on 2024-07-29 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references_app', '0002_opf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opf',
            name='parent_id',
            field=models.IntegerField(unique=True),
        ),
    ]