# Generated by Django 5.0.7 on 2024-07-26 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0005_rename_rut_usuario_rut"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="direccion",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="web.direccion",
            ),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="tipo_usuario",
            field=models.CharField(
                choices=[
                    ("arrendatario", "Arrendatario"),
                    ("arrendador", "Arrendador"),
                ],
                default="arrendatario",
                max_length=12,
            ),
        ),
    ]