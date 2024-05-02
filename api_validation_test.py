import unittest
import requests

class TestAPIValidationAddToCart(unittest.TestCase):
    base_url = "http://localhost:5000"  # Update with the base URL of your API

    def test_add_to_cart(self):
        # Define the payload for adding a product to the cart
        cart_data = {
            "product_id": 1,  # Specify the ID of the product to add to the cart
            "quantity": 1  # Specify the quantity of the product to add
        }

        # Send a POST request to add a product to the cart
        response = requests.post(f"{self.base_url}/cart/add", json=cart_data)
        
        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Assert that the response contains JSON data
        self.assertTrue(response.headers.get("content-type").startswith("application/json"))

        # Add more assertions to validate the structure and content of the response data as needed

if __name__ == "__main__":
    unittest.main()
