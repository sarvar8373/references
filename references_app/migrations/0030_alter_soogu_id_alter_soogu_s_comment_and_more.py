# Generated by Django 5.0.6 on 2024-07-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references_app', '0029_alter_soogu_id_alter_soogu_s_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soogu',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='soogu',
            name='s_comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='soogu',
            name='s_status',
            field=models.CharField(max_length=10),
        ),
    ]