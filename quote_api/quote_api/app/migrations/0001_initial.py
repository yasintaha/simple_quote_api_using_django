# Generated by Django 2.1.5 on 2019-01-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=243)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
