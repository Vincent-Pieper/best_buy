import products


class Store:
    """Represent a store that manages products."""

    def __init__(self, product_list: list[products.Product]) -> None:
        self.products = product_list

    def add_product(self, product: products.Product) -> None:
        """Adds a product to the store"""
        self.products.append(product)

    def remove_product(self, product: products.Product) -> None:
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
        combined_order = self._combine_shopping_list(shopping_list)
        self._validate_order(combined_order)
        return self._buy_order(combined_order)


    def _combine_shopping_list(self, shopping_list) -> dict:
        """Combine duplicate products in the shopping list."""
        combined_order = {}

        for product, quantity in shopping_list:
            if product in combined_order:
                combined_order[product] += quantity
            else:
                combined_order[product] = quantity

        return combined_order


    def _validate_order(self, combined_order) -> None:
        """Validate that the complete order can be bought."""
        for product, quantity in combined_order.items():
            if quantity <= 0:
                raise ValueError("Purchase quantity must be positive.")
            if quantity > product.get_quantity():
                raise ValueError("Not enough quantity in stock.")
            if not product.is_active():
                raise ValueError("Product is not active.")

    def _buy_order(self, combined_order) -> float:
        """Buy all products in the combined order and return the total price."""
        total_amount = 0

        for product, quantity in combined_order.items():
            total_amount += product.buy(quantity)

        return total_amount


def main() -> None:
    """Runs a local test for store.py"""
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
