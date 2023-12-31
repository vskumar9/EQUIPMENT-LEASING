# Generated by Django 4.0.8 on 2023-06-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.BigIntegerField()),
                ('Address', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=20)),
                ('TermAndConditions', models.BooleanField(default=True)),
            ],
        ),
    ]
