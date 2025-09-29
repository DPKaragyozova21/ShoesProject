
class CatalogService:
    def __init__(self):
        self.products = []
        self.next_id = 1



    def add_product(self, product_data):
        product = {
            'id': self.next_id,
            **product_data
        }
        self.products.append(product)
        self.next_id += 1
        return product

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def update_product(self, product_id, product_data):
        for i, product in enumerate(self.products):
            if product['id'] == product_id:
                self.products[i] = {'id': product_id, **product_data}
                return True
        return False

    def delete_product(self, product_id):
        self.products = [p for p in self.products if p['id'] != product_id]

    def search_products(self, search='', color='', min_price=None, max_price=None, size=''):
        results = self.products

        if search:
            results = [p for p in results if
                       search.lower() in p['name'].lower() or search.lower() in p['color'].lower()]

        if color:
            results = [p for p in results if p['color'].lower() == color.lower()]

        if min_price is not None:
            results = [p for p in results if p['price'] >= min_price]

        if max_price is not None:
            results = [p for p in results if p['price'] <= max_price]

        if size:
            results = [p for p in results if size in p['sizes']]

        return results

    def get_all_colors(self):
        return list(set(p['color'] for p in self.products))

    def get_all_sizes(self):
        sizes = set()
        for product in self.products:
            sizes.update(product['sizes'])
        return sorted(list(sizes))

    def reduce_stock(self, product_id, quantity=1):
        for product in self.products:
            if product['id'] == product_id and product['stock'] >= quantity:
                product['stock'] -= quantity
                return True
        return False


catalog_service = CatalogService()