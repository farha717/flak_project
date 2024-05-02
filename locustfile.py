from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def add_to_cart(self):
        product_id = 1  # Specify the ID of the product you want to add to cart
        self.client.post(f'/cart/add', json={"product_id": product_id, "quantity": 1})

    @task
    def view_cart(self):
        self.client.get('/cart')

    # Add more tasks to simulate different user behaviors

