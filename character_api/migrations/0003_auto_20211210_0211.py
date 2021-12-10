# Generated by Django 3.2.7 on 2021-12-10 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character_api', '0002_auto_20211210_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='roles',
        ),
        migrations.AddField(
            model_name='character',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='character_api.role'),
        ),
    ]