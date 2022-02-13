# Generated by Django 4.0.1 on 2022-02-13 03:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='名前')),
                ('price', models.FloatField(verbose_name='価格')),
                ('text', models.CharField(blank=True, max_length=200, verbose_name='説明')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='編集日時')),
                ('artist', models.CharField(max_length=100, verbose_name='アーティスト')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='いいね')),
            ],
        ),
    ]
