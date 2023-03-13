# Generated by Django 4.1.7 on 2023-03-13 13:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("copies", "0005_alter_loan_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="copy",
            name="loans",
            field=models.ManyToManyField(
                related_name="copies",
                through="copies.Loan",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
