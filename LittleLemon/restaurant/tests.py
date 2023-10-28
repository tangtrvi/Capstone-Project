from django.test import TestCase
from .models import menu, booking

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

class BookingViewTest(TestCase):
    def setUp(self):
        # return f'- {self.booking_date} : {self.name} ({str(self.no_of_guest)} guests)'
        booking.objects.create(name="James", no_of_guest=2, booking_date="2023-10-28T20:19:00Z")
        booking.objects.create(name="Kelm", no_of_guest=6, booking_date="2023-10-27T13:19:00Z")

    def test_getall(self):
        iceCream = booking.objects.get(name="James")
        cake = booking.objects.get(name="Kelm")

        self.assertEqual(iceCream.get_detail(), '- 2023-10-28 20:19:00+00:00 : James (2 guests)')
        self.assertEqual(cake.get_detail(), '- 2023-10-27 13:19:00+00:00 : Kelm (6 guests)')

