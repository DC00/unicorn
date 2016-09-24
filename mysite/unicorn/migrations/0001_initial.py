# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('headline', models.CharField(max_length=100)),
                ('abstract', models.TextField(max_length=100)),
                ('copy', models.TextField(max_length=300)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=140)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('headshot', models.ImageField(blank=True, null=True, upload_to='headshots')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=140)),
                ('academic_year', models.IntegerField()),
                ('school', models.CharField(choices=[('SEAS', 'School of Engineering and Applied Sciences'), ('BATTEN', 'Frank Batten School of Leadership and Public Policy'), ('CLAS', 'College of Arts and Sciences'), ('CURRY', 'Curry School of Education'), ('Darden', 'Darden School of Business'), ('COMM', 'McIntire School of Commerce'), ('SARC', 'School of Architecture'), ('SCPS', 'School of Continuing and Professional Studies'), ('LAW', 'School of Law'), ('MED', 'School of Medicine'), ('NURSE', 'School of Nursing')], max_length=100)),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=32, unique=True)),
                ('description', models.CharField(default='', max_length=140)),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(related_name='articles', to='unicorn.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.ManyToManyField(blank=True, to='unicorn.ArticleImage'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='unicorn.Tag'),
        ),
    ]
