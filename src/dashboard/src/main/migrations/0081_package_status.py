# Generated by Django 1.11.29 on 2021-05-17 18:39
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0080_delete_software_agent"),
    ]

    operations = [
        migrations.AddField(
            model_name="sip",
            name="completed_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="sip",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Unknown"),
                    (1, "Processing"),
                    (2, "Done"),
                    (3, "Completed successfully"),
                    (4, "Failed"),
                ],
                db_column="status",
                default=0,
            ),
        ),
        migrations.AddField(
            model_name="transfer",
            name="completed_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="transfer",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Unknown"),
                    (1, "Processing"),
                    (2, "Done"),
                    (3, "Completed successfully"),
                    (4, "Failed"),
                ],
                db_column="status",
                default=0,
            ),
        ),
    ]
