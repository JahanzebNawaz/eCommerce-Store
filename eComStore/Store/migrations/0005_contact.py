# Generated by Django 2.2.7 on 2019-12-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_auto_20191130_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
