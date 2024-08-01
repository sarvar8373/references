# Generated by Django 5.0.6 on 2024-07-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references_app', '0037_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='NATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField()),
                ('s_comment', models.TextField(blank=True, null=True)),
                ('s_create', models.DateTimeField(blank=True, null=True)),
                ('s_status', models.CharField(max_length=10)),
                ('name_ru', models.CharField(max_length=255)),
                ('name_uz', models.CharField(max_length=255)),
                ('name_uzl', models.CharField(max_length=255)),
                ('s_user_id', models.IntegerField()),
            ],
        ),
    ]
