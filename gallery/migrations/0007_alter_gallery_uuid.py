# Generated by Django 4.0.6 on 2022-07-21 08:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_alter_gallery_uuid_alter_gallery_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b6e5d7ea-5816-41f5-bbcd-a3ad9bf04479'), primary_key=True, serialize=False),
        ),
    ]
