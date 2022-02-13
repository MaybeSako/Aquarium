from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
# class NFT(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     price = models.FloatField(verbose_name='価格')
#     name = models.CharField(verbose_name='名前', max_length=40)
#     text = models.CharField(verbose_name='説明', max_length=200, blank=True, null=False)
#     created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name='編集日時', auto_now=True)
#     artist = models.CharField(verbose_name='アーティスト', max_length=100)
#     likes = models.PositiveIntegerField(verbose_name='いいね', default=0)