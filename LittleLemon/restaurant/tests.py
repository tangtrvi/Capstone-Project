from django.test import TestCase
from .models import menu

# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        menu.objects.create(title="IceCream", price=80, inventory=100)
        menu.objects.create(title="Cake", price=15.3, inventory=20)

    def test_getall(self):
        iceCream = menu.objects.get(title="IceCream")
        cake = menu.objects.get(title="Cake")
        
        self.assertEqual(iceCream.get_item(), "IceCream : 80.00")
        self.assertEqual(cake.get_item(), "Cake : 15.30")
