# Generated by Django 3.2.5 on 2021-07-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registeration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('birthdate', models.TextField()),
                ('emial', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]