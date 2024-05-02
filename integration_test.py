import unittest
from app import app

class TestIntegrationAddToCart(unittest.TestCase):
    def setUp(self):
        # Set up test client
        self.client = app.test_client()
        # Create a test product in the database
        self.product_id = self.create_test_product()

    def create_test_product(self):
        # Create a test product in the database and return its ID
        response = self.client.post('/products', json={"name": "Test Product", "price": 9.99})
        data = response.json
        return data['id']

    def tearDown(self):
        # Clean up test product from the database
        self.client.delete(f'/products/{self.product_id}')

    def test_add_to_cart_and_get_cart_details(self):
        # Test adding a product to the cart and then retrieving cart details
        # Add a product to the cart
        response = self.client.post('/cart/add', json={"product_id": self.product_id, "quantity": 1})
        self.assertEqual(response.status_code, 201)  # Check if product is added to cart successfully

        # Retrieve details of the cart
        response = self.client.get('/cart')
        self.assertEqual(response.status_code, 200)  # Check if request is successful

        # Check if the retrieved cart details contain the added product
        data = response.json
        self.assertTrue(any(item['id'] == self.product_id for item in data))

if __name__ == '__main__':
    unittest.main()
