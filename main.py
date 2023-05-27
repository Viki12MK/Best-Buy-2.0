import products
import store

# Setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)]

best_buy = store.Store(product_list)


def list_all_products(best_buy):
    products = best_buy.get_all_products()
    if not products:
        print("No products available in the store.")
    else:
        for product in products:
            print(product.show())


def start(best_buy):
    order = []
    while True:
        print("   Store Menu")
        print("   " + "-" * 10)
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            print("-" * 10)
            # List all products in the store
            list_all_products(best_buy)
            print("-" * 10)

        elif choice == '2':
            # Show total amount in store
            total_quantity = best_buy.get_total_quantity()
            print(f"Total items in store: {total_quantity}")

        elif choice == '3':
            print("Product list:")
            list_all_products(best_buy)
            print("-" * 50)

            while True:
                # Make an order
                product_name = input("Enter the product name: ")
                quantity = int(input("Enter the product amount: "))
                order.append((product_name, quantity))
                more_orders = input("Do you want to continue shopping? "
                                    "(Press 'y' to continue or any other key to quit)")

                if more_orders.lower() != 'y':
                    break

            print("Order summary:")
            total_price = 0
            for item in order:
                product_name, quantity = item
                product = None
                for prod in best_buy.products:
                    if prod.name.lower() == product_name.lower():
                        product = prod
                        break

                if product:
                    try:
                        total_price += product.buy(quantity)
                        print(f"Product: {product_name}, Quantity: {quantity}, Price: ${product.price * quantity}")
                    except Exception as e:
                        print(str(e))
                else:
                    print(f"Product {product_name} not found in the store.")

            print(f"Total price: ${total_price}")
            break

        elif choice == '4':
            # Quit
            print("Thank you for using our e-store")
            break
        print()


start(best_buy)
