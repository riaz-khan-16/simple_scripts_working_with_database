# Generated by Django 4.2.5 on 2023-09-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20, null=True)),
                ('position', models.CharField(max_length=20, null=True)),
                ('salary', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]