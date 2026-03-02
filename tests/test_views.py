from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(Title="Pizza", Price=12.99, Inventory=50)
        Menu.objects.create(Title="Burger", Price=8.50, Inventory=30)
        Menu.objects.create(Title="Pasta", Price=10.75, Inventory=40)

    def test_getall(self):
        # Retrieve all Menu objects
        menu_items = Menu.objects.all()
        
        # Serialize the data
        serializer = MenuSerializer(menu_items, many=True)
        
        # Get the response from the view
        response = self.client.get('/restaurant/menu/')
        
        # Compare serialized data with response data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
