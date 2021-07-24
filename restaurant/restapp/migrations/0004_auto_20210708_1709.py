# Generated by Django 3.0 on 2021-07-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0003_rolereq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolereq',
            name='rltype',
            field=models.IntegerField(choices=[(2, 'manager'), (3, 'user')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'guest'), (2, 'manager'), (3, 'user')], default=1, max_length=10),
        ),
    ]
