from cache import CachedOrderRepository
from agregator import Order, Product


def main():
    database_name = "bookstore.db"
    repo = CachedOrderRepository(database_name)

    while True:
        print("1. Create Order")
        print("2. Load Order")
        print("3. Load All Orders")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            order = create_order()
            repo.save_order(order)
            print("Order created and saved.")
        elif choice == "2":
            order_id = int(input("Enter order ID: "))
            order = repo.load_order(order_id)
            if order:
                print("Order ID:", order.id)
                print("Total:", order.calculate_total())
            else:
                print("Order not found.")
        elif choice == "3":
            orders = repo.load_all_orders()
            for order in orders:
                print("Order ID:", order.id)
                print("Total:", order.calculate_total())
                print("-" * 20)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose again.")


def create_order():
    order_id = int(input("Enter order ID: "))
    order = Order(order_id)
    while True:
        product_id = int(input("Enter product ID (0 to finish): "))
        if product_id == 0:
            break
        quantity = int(input("Enter quantity: "))
        # Replace with actual product data
        product = Product(product_id, f"Product {product_id}", 10.0)
        order.add_item(product, quantity)
    return order


if __name__ == "__main__":
    main()
