# Generated by Django 3.1.1 on 2020-09-17 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Universal_cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('cases', models.IntegerField()),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]