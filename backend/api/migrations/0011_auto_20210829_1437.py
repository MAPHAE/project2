# Generated by Django 3.1.2 on 2021-08-29 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210829_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='consumedOnFull',
            new_name='consumeOnFull',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='ffrom',
            new_name='frrom',
        ),
    ]
