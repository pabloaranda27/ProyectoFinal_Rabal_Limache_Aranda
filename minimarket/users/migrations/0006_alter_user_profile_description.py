# Generated by Django 4.0.6 on 2022-09-04 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]