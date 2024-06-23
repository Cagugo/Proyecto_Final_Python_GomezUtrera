from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):

    def setUp(self):
        Product.objects.create(title="Test Product", brand="Test Brand", price=100, author_id=1, image="test_image.jpg")

    def test_product_creation(self):
        product = Product.objects.get(title="Test Product")
        self.assertEqual(product.brand, "Test Brand")
        self.assertEqual(product.price, 100)
