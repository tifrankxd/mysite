# Generated by Django 4.2.5 on 2023-11-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_sociallink'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='social_icons/'),
        ),
    ]
