# Generated by Django 4.2.5 on 2023-11-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_contact_remove_sociallink_icon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
