# Generated by Django 4.2 on 2023-05-02 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='domains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, unique=True)),
                ('Description', models.CharField(default=None, max_length=15)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('visitor', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Domain',
                'verbose_name_plural': 'Custom Domain',
            },
        ),
        migrations.CreateModel(
            name='pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('visitor', models.IntegerField(default=0)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.domains')),
            ],
            options={
                'verbose_name': 'Pages',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
