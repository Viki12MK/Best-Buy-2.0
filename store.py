class Store:
    def __init__(self, product_list):
        self.products = product_list

    # Add product to store
    def add_product(self, product):
        self.products.append(product)

    # Remove product from store
    def remove_product(self, product):
        self.products.remove(product)

    # Returns how many items are in the store in total
    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    # Returns all active products in the store -> List[Product]
    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    # Get a list of tuples, where each tuple has two items: Product(product class) and quantity(int)
    def order(self, shopping_list):
        ordered_products = []
        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                available_quantity = min(quantity, product.get_quantity())
                ordered_products.append((product, available_quantity))
        return ordered_products
