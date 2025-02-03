# Generated by Django 4.2.2 on 2025-02-01 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_rename_customer_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Введите номер телефона",
                max_length=35,
                null=True,
                verbose_name="Номер телефона",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="tg_name",
            field=models.CharField(
                blank=True,
                help_text="Введите ник телеграмма",
                max_length=50,
                null=True,
                verbose_name="Ник телеграм",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Token"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите свой аватар",
                null=True,
                upload_to="users/avatars/",
                verbose_name="Аватар",
            ),
        ),
        migrations.AlterModelTable(
            name="user",
            table=None,
        ),
    ]
