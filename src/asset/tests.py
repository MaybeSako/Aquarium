import datetime

from django.test import TestCase

from .models import Asset


class AssetModelTests(TestCase):

    def test_asset_has_date(self):
        """
        作成した日記データに日付が付与されているか確認        
        """
        Asset.objects.create(name='Tesla', price=100)
        actual_asset = Asset.objects.get(name='Tesla')
        self.assertIsInstance(actual_asset.created_at, datetime.date)

    def test_save_and_retrieve(self):
        """
        日記データの保存と取得を確認
        """
        Asset.objects.create(name='Tesla', price=100)
        actual_asset = Asset.objects.get(name='Tesla')
        self.assertEqual(actual_asset.name, 'Tesla')
