# Generated by Django 4.1.7 on 2023-03-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_helprequest_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="helprequest",
            name="type",
            field=models.CharField(
                choices=[
                    ("FOOD", "FOOD"),
                    ("MEDICINE", "MEDICINE"),
                    ("CLOTHES", "CLOTHES"),
                    ("SHELTER", "SHELTER"),
                    ("RESCUE", "RESCUE"),
                    ("MISSING", "MISSING"),
                    ("OTHER", "OTHER"),
                ],
                max_length=100,
            ),
        ),
    ]