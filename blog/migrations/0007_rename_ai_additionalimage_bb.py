# Generated by Django 3.2.3 on 2021-05-16 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_additionalimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalimage',
            old_name='ai',
            new_name='bb',
        ),
    ]
