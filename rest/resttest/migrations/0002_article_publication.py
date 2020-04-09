# Generated by Django 3.0.5 on 2020-04-04 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resttest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='resttest.Publication')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]