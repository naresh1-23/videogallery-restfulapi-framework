# Generated by Django 4.0.6 on 2022-07-21 08:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_alter_gallery_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1b5ec25d-dccb-49ad-a6e3-c9f79685541e'), primary_key=True, serialize=False),
        ),
    ]
