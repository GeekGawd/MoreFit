# Generated by Django 4.0.2 on 2022-02-27 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_muscle_category_muscle_type_of_muscle'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='gender',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
