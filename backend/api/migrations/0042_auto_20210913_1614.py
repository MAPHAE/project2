# Generated by Django 3.1.2 on 2021-09-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0041_merge_20210913_1128"),
    ]

    operations = [
        migrations.AlterField(
            model_name="spell_match_performance",
            name="summoner_level",
            field=models.CharField(default="", max_length=100),
        ),
    ]
