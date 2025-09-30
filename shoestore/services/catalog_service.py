class CatalogService:
    def __init__(self):
        self.products = []
        self.categories = []
        self.next_id = 1
        self.next_category_id = 1
        self.initialize_categories()

    def initialize_categories(self):

        categories_data = [
            {'name': 'Дамски обувки'},
            {'name': 'Мъжки обувки'},
            {'name': 'Детски обувки'}
        ]

        for cat_data in categories_data:
            category = {
                'id': self.next_category_id,
                'name': cat_data['name'],

            }
            self.categories.append(category)
            self.next_category_id += 1

    def get_all_categories(self):

        return self.categories

    def get_category_by_id(self, category_id):

        for category in self.categories:
            if category['id'] == category_id:
                return category
        return None

    def initialize_sample_data(self):
        sample_products = [

            {
                'name': 'Nike Air Force 1',
                'description': 'Classic white basketball sneakers with premium leather upper',
                'color': 'White',
                'price': 140.00,
                'stock': 68,
                'image_url': 'https://static.ftshp.digital/img/p/6/7/6/0/5/4/676054.jpg',
                'sizes': ['35', '36', '37', '38', '39', '40', '41'],
                'category_id': 1
            },
            {
                'name': 'Nike Court Vision Lo',
                'description': 'Розови дамски маратонки с ретро дизайн',
                'color': 'Pink',
                'price': 85.99,
                'stock': 45,
                'image_url': 'https://th.bing.com/th/id/OPEC.srXr7mpZyJLf4Q474C474?w=248&h=248&c=17&o=5&pid=21.1',
                'sizes': ['35', '36', '37', '38', '39', '40', '41'],
                'category_id': 1
            },
            {
                'name': 'Puma Suede Classic',
                'description': 'Vintage suede sneakers with bold blue colorway',
                'color': 'Blue',
                'price': 89.99,
                'stock': 41,
                'image_url': 'https://static.qns.digital/img/p/2/6/0/0/7/3/1/2600731.jpg',
                'sizes': ['35', '36', '37', '38', '39', '40'],
                'category_id': 1
            },


            {
                'name': 'Adidas Stan Smith',
                'description': 'Legendary white tennis sneakers with green accents',
                'color': 'White',
                'price': 95.50,
                'stock': 52,
                'image_url': 'https://th.bing.com/th?id=OPEC.m%2bE8cBUJKZW3ew474C474&w=248&h=248&c=17&o=5&pid=21.1',
                'sizes': ['40', '41', '42', '43', '44', '45'],
                'category_id': 2
            },
            {
                'name': 'Converse Chuck Taylor All Star',
                'description': 'Iconic high-top canvas sneakers in classic black',
                'color': 'Black',
                'price': 65.00,
                'stock': 73,
                'image_url': 'https://th.bing.com/th?id=OPEC.tzM3w8%2bHQUtbKg474C474&w=200&h=213&c=17&pid=21.1',
                'sizes': ['40', '41', '42', '43', '44', '45'],
                'category_id': 2
            },
            {
                'name': 'Vans Old Skool',
                'description': 'Skate shoes with signature side stripe in navy blue',
                'color': 'Navy',
                'price': 79.99,
                'stock': 34,
                'image_url': 'https://static.ftshp.digital/img/p/1/4/9/9/2/8/4/1499284.jpg',
                'sizes': ['40', '41', '42', '43', '44'],
                'category_id': 2
            },
            {
                'name': 'New Balance 574',
                'description': 'Retro running shoes with suede and mesh construction',
                'color': 'Grey',
                'price': 120.00,
                'stock': 28,
                'image_url': 'https://th.bing.com/th/id/OPEC.xJfInKz7dj3tiA474C474?w=160&h=213&c=17&pid=21.1',
                'sizes': ['40', '41', '42', '43', '44', '45'],
                'category_id': 2
            },
            {
                'name': 'Dr. Martens 1460',
                'description': 'Classic 8-eye leather boots with yellow stitching',
                'color': 'Black',
                'price': 189.99,
                'stock': 19,
                'image_url': 'https://static.ftshp.digital/img/p/8/2/0/5/2/2/820522.jpg',
                'sizes': ['40', '41', '42', '43', '44', '45'],
                'category_id': 2
            },
            {
                'name': 'Timberland 6-Inch Premium',
                'description': 'Waterproof nubuck leather boots in wheat color',
                'color': 'Wheat',
                'price': 199.00,
                'stock': 15,
                'image_url': 'https://static.ftshp.digital/img/p/1/2/9/9/7/0/9/1299709.jpg',
                'sizes': ['40', '41', '42', '43', '44', '45'],
                'category_id': 2
            },
            {
                'name': 'Jordan 1 Retro High',
                'description': 'Legendary basketball sneakers in classic red and white',
                'color': 'Red',
                'price': 170.00,
                'stock': 22,
                'image_url': 'https://tse1.mm.bing.net/th/id/OIP.0FqJNTN9m6TvB3gRVUnZIwHaFS?rs=1&pid=ImgDetMain&o=7&rm=3',
                'sizes': ['40', '41', '42', '43', '44', '45'],
                'category_id': 2
            },


            {
                'name': 'Nike Kids Air Force',
                'description': 'Детски маратонки в бяло и розово',
                'color': 'White',
                'price': 65.00,
                'stock': 30,
                'image_url': 'https://static.ftshp.digital/img/p/6/7/6/0/5/4/676054.jpg',
                'sizes': ['28', '29', '30', '31', '32', '33', '34'],
                'category_id': 3
            },
            {
                'name': 'Adidas Kids Superstar',
                'description': 'Класически детски маратонки',
                'color': 'White',
                'price': 55.00,
                'stock': 25,
                'image_url': 'https://th.bing.com/th?id=OPEC.m%2bE8cBUJKZW3ew474C474&w=248&h=248&c=17&o=5&pid=21.1',
                'sizes': ['28', '29', '30', '31', '32', '33', '34'],
                'category_id': 3
            }
        ]

        for product_data in sample_products:
            self.add_product(product_data)

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

    def search_products(self, search='', color='', min_price=None, max_price=None, size='', category_id=None):
        results = self.products


        if category_id:
            results = [p for p in results if p.get('category_id') == category_id]

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