# Generated by Django 4.1.7 on 2023-03-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="loan",
            old_name="user",
            new_name="account",
        ),
        migrations.AddField(
            model_name="copy",
            name="last_loan",
            field=models.DateTimeField(default=None, null=True),
        ),
    ]