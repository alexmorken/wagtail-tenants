# Generated by Django 3.2.10 on 2021-12-17 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_tenants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
