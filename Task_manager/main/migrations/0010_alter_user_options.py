# Generated by Django 4.0.5 on 2022-06-12 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_alter_task_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "пользователя",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
