import products
import store
import sys


def start(store_instance: store.Store) -> None:
    """Run the store menu program."""
    while True:
        print("   Store Menu")
        print("   ----------")
        menu = get_menu()
        choice = choose_from_options(menu)
        actions = get_menu_actions()
        action = actions[choice]
        action(store_instance)


def get_menu() -> dict[str, str]:
    """Return the main menu options."""
    return {
        "1": "List all products in store",
        "2": "Show total amount in store",
        "3": "Make an order",
        "4": "Quit"
    }


def choose_from_options(options: dict[str, str]) -> str:
    """Display menu options and return a valid selected choice."""
    check = False
    biggest_number = 0
    while not check:

        for key, value in options.items():
            print(f"{key}. {value}")
            biggest_number = key

        choice = input(
            f"Please choose a number (1-{biggest_number}) : "
        )

        check = validate_number_input(
            choice,
            int,
            (1, int(biggest_number))
        )

    return choice


def validate_number_input(
        user_input: str,
        expected_type: type[int] | type[float],
        choice_range: tuple[int, int] | None = None
) -> bool:
    """Validate numeric input against an optional allowed range."""
    if choice_range is not None:
        lowest_number, biggest_number = choice_range

        try:
            if (
                    expected_type in (int, float)
                    and lowest_number
                    <= expected_type(user_input)
                    <= biggest_number
            ):
                return True

            print(
                f"Only use numbers between "
                f"{lowest_number} and {biggest_number}"
            )
        except ValueError:
            print(
                f"Only use numbers between "
                f"{lowest_number} and {biggest_number}"
            )

    return False


def get_menu_actions() -> dict[str, object]:
    """Return menu choices mapped to functions."""
    return {
        "1": show_active_products,
        "2": show_total_amount,
        "3": make_order,
        "4": terminate_program
    }


def show_active_products(store_instance: store.Store) -> None:
    """Print all active products in the store."""
    active_products = store_instance.get_all_products()
    print_product_menu(active_products)


def print_product_menu(
        active_products: list,
        include_checkout: bool = False
) -> tuple[dict, int]:
    """Print active products and return a product menu plus checkout number."""
    product_menu = {}

    print("\n------")

    for counter, product in enumerate(active_products, start=1):
        print(f"{counter}. ", end="")
        product.show()
        product_menu[str(counter)] = product

    checkout_number = len(active_products) + 1

    if include_checkout:
        print(f"{checkout_number}. # Check-Out #")

    print("------\n")

    return product_menu, checkout_number


def show_total_amount(store_instance: store.Store) -> None:
    """Print the total quantity of all products in the store."""
    print(f"\nTotal of {store_instance.get_total_quantity()} items in store\n")


def make_order(store_instance: store.Store) -> None:
    """Let the user build a shopping list and check out the order."""
    active_products = store_instance.get_all_products()
    order_menu, checkout_number = print_product_menu(
        active_products,
        include_checkout=True
    )

    shopping_list = []

    while True:
        product_choice = get_product_choice(checkout_number)

        if int(product_choice) == checkout_number:
            checkout_order(store_instance, shopping_list)
            return None

        product_amount = get_product_amount()
        shopping_list.append((order_menu[product_choice], product_amount))
        print(f"[{product_amount}*] {order_menu[product_choice].name} added to the list!\n")


def get_product_choice(biggest_number: int) -> str:
    """Ask for a valid product menu choice and return it."""
    while True:
        product_choice = input("Which product # do you want? ")

        valid_input = validate_number_input(
            product_choice,
            int,
            (1, biggest_number)
        )

        if not valid_input:
            print("Error adding product!")
            continue

        return product_choice


def checkout_order(
        store_instance: store.Store,
        shopping_list: list[tuple[object, int]]
) -> None:
    """Buy all products in the shopping list and print the total price."""
    try:
        print("\n********")
        print(f"Order made! Total payment: ${store_instance.order(shopping_list)}\n")
    except ValueError as error:
        print(f"Order failed: {error}\n")


def get_product_amount() -> int:
    """Ask for a positive product amount and return it."""
    while True:
        product_amount = input("What amount do you want? ")

        try:
            product_amount = int(product_amount)
            if product_amount <= 0:
                print("Only use positive numbers")
                continue

            return product_amount

        except ValueError:
            print("Only use positive numbers")


def terminate_program(_: store.Store) -> None:
    """Print the exit message and stop the program."""
    print("\nGood bye! - Guten Einkauf!")
    sys.exit()


def main() -> None:
    """Set up the store and start the user interface."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
