# Generated by Django 3.2.9 on 2021-11-24 13:47

from django.db import migrations
import wagtail_tenants.users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="TenantGroup",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth.group",),
            managers=[
                ("objects", wagtail_tenants.users.models.TenantGroupManager()),
            ],
        ),
    ]
