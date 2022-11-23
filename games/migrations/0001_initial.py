# Generated by Django 4.1.3 on 2022-11-23 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ['-platform'],
            },
        ),
    ]
