# Generated by Django 4.0.6 on 2022-07-21 08:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_alter_gallery_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b2bea91c-6649-476a-8398-01802d4c8d0d'), primary_key=True, serialize=False),
        ),
    ]
