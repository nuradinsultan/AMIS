# backend/inventory/tests.py

from django.test import TestCase
from .models import InventoryItem

class InventoryItemModelTest(TestCase):
    def setUp(self):
        InventoryItem.objects.create(name="Test Item", quantity=10)

    def test_inventory_item_creation(self):
        item = InventoryItem.objects.get(name="Test Item")
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.quantity, 10)
