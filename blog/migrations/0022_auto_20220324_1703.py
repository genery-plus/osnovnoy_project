# Generated by Django 3.2.6 on 2022-03-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_character_worldview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='hair',
        ),
        migrations.AlterField(
            model_name='character',
            name='character_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='hit_points_damage_reduction',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='hit_points_nonlethal_damage',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='hit_points_total',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='hit_points_wounds_current_HP',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='thedeity',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='weight',
            field=models.TextField(blank=True),
        ),
    ]
