# Generated by Django 3.2.6 on 2022-03-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20220324_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='worldview',
            field=models.TextField(blank=True, null=True),
        ),
    ]
