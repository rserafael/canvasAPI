# Generated by Django 2.0.7 on 2018-08-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookupload', '0002_auto_20180806_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField()),
                ('Y', models.FloatField()),
                ('MODE', models.BooleanField()),
                ('COLOR', models.CharField(max_length=500)),
                ('WIDTH', models.BigIntegerField()),
                ('SIZE', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='DATE',
        ),
        migrations.RemoveField(
            model_name='book',
            name='FILE',
        ),
        migrations.RemoveField(
            model_name='book',
            name='TYPE',
        ),
        migrations.AddField(
            model_name='object',
            name='stack',
            field=models.ForeignKey(on_delete=None, to='bookupload.Stack'),
        ),
    ]