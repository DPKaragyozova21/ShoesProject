
from services.catalog_service import catalog_service


class CartService:
    def __init__(self):
        self.carts = {}

    def add_to_cart(self, user_email, product_id, size):
        product = catalog_service.get_product_by_id(product_id)
        if not product or product['stock'] <= 0 or size not in product['sizes']:
            return False

        if user_email not in self.carts:
            self.carts[user_email] = []


        for item in self.carts[user_email]:
            if item['product']['id'] == product_id and item['size'] == size:
                item['quantity'] += 1
                return True


        cart_item = {
            'product': product,
            'size': size,
            'quantity': 1
        }
        self.carts[user_email].append(cart_item)
        return True

    def get_cart(self, user_email):
        return self.carts.get(user_email, [])

    def get_cart_total(self, user_email):
        cart_items = self.get_cart(user_email)
        return sum(item['product']['price'] * item['quantity'] for item in cart_items)

    def clear_cart(self, user_email):
        if user_email in self.carts:
            del self.carts[user_email]


cart_service = CartService()