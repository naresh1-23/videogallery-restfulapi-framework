# Generated by Django 4.0.6 on 2022-07-21 07:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_gallery_uuid_alter_gallery_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9b050f7b-04b6-48d5-a826-76b9eb3d4961'), primary_key=True, serialize=False),
        ),
    ]
