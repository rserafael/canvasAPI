# Generated by Django 2.0.7 on 2018-08-04 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=500)),
                ('TYPE', models.CharField(max_length=500)),
                ('SIZE', models.BigIntegerField()),
                ('DATE', models.FloatField()),
                ('FILE', models.FileField(upload_to='')),
            ],
        ),
    ]
