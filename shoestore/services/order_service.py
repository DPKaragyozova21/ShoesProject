from services.cart_service import cart_service
from services.catalog_service import catalog_service
from datetime import datetime


class BaseService:

    def __init__(self):
        self.next_id = 1

    def get_next_id(self):
        current_id = self.next_id
        self.next_id += 1
        return current_id

    def log_action(self, action):
        print(f"[BaseService] {action}")


class OrderService(BaseService):
    def __init__(self):
        super().__init__()
        self.orders = []

    def create_order(self, user_email, address, payment_method):
        cart_items = cart_service.get_cart(user_email)

        if not cart_items:
            return False

        for item in cart_items:
            product_id = item['product']['id']
            quantity = item['quantity']

            if not catalog_service.reduce_stock(product_id, quantity):
                return False

        order = {
            'id': self.get_next_id(),
            'user_email': user_email,
            'items': cart_items.copy(),
            'address': address,
            'payment_method': payment_method,
            'total': cart_service.get_cart_total(user_email),
            'created_at': datetime.now()
        }

        self.orders.append(order)
        self.log_action(f"Order created for: {user_email}")
        print(f"Order confirmation sent to: {user_email}")
        return True

    def get_orders_by_user(self, user_email):
        return [order for order in self.orders if order['user_email'] == user_email]

    def log_action(self, action):
        print(f"[OrderService] {action}")


order_service = OrderService()