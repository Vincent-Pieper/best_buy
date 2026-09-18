class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Sets the quantity and deactivates the product if it reaches 0."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self) -> None:
        """Activates the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the product."""
        self.active = False

    def show(self) -> None:
        """Prints the product information."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Buys a quantity of the product and returns the total price."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        if not self.active:
            raise ValueError("Product is not active.")

        self.set_quantity(self.quantity - quantity)
        return quantity * self.price
