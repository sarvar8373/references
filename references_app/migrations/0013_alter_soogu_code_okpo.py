# Generated by Django 5.0.6 on 2024-07-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references_app', '0012_alter_soogu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soogu',
            name='code_okpo',
            field=models.CharField(max_length=255),
        ),
    ]
