# Generated by Django 3.2.6 on 2022-03-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_character_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='lvlcharacter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='srtength_ability_modifier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='srtength_ability_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='thedeity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
