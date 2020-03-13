# Generated by Django 3.0.3 on 2020-03-13 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='no username', max_length=45)),
                ('bodyText', models.CharField(default='no body text', max_length=200)),
                ('dateCreated', models.DateTimeField(default='', verbose_name='datePosted')),
                ('likes', models.IntegerField(default=0)),
                ('userId', models.CharField(default='@', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=25)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.Post')),
            ],
        ),
    ]