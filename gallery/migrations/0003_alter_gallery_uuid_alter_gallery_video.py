# Generated by Django 4.0.6 on 2022-07-21 07:52

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_gallery_uuid_alter_gallery_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a3ed26ed-98f9-4599-959b-3ceb48c8afa2'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='video',
            field=models.FileField(upload_to='videos', validators=[django.core.validators.FileExtensionValidator('mp4')]),
        ),
    ]
