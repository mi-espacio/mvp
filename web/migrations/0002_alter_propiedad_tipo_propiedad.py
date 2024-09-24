# Generated by Django 5.0.7 on 2024-07-19 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="propiedad",
            name="tipo_propiedad",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="propiedad",
                to="web.tipopropiedad",
            ),
        ),
    ]