# Generated by Django 5.0.6 on 2024-06-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
