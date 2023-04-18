# Generated by Django 4.2 on 2023-04-18 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("EventixApp", "0002_ticket_event_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wrap",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EventixApp.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Card",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("context", models.JSONField(default=list)),
                (
                    "wrap",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EventixApp.wrap",
                    ),
                ),
            ],
        ),
    ]
