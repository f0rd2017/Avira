# Generated by Django 4.0.4 on 2022-06-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_users_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='count',
            field=models.CharField(default=0, max_length=50, verbose_name='Кількість токенів'),
            preserve_default=False,
        ),
    ]