# Generated by Django 3.2.10 on 2023-01-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VR_Chest_App', '0016_auto_20221231_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]