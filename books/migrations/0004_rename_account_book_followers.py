# Generated by Django 4.1.7 on 2023-03-09 22:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_rename_user_follow_account"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="account",
            new_name="followers",
        ),
    ]
