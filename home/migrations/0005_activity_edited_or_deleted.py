# Generated by Django 4.2.3 on 2023-09-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_activity_options_activity_modified_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='edited_or_deleted',
            field=models.CharField(default='Deleted', max_length=255),
            preserve_default=False,
        ),
    ]
