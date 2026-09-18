import products


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from store"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total"""
        num_of_products = 0
        for product in self.products:
            num_of_products += product.get_quantity()
        return num_of_products

    def get_all_products(self) -> list[products.Product]:
        """Returns all products in the store that are active"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list) -> float:
        """Buys the products and returns the total price of the order."""
        total_amount = 0
        for product, quantity in shopping_list:
            total_amount += product.buy(quantity)

        return total_amount



def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()