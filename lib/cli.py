from helpers import print_menu, get_input
from db.models import Order, Product

def main_menu():
    options = {
        "1": "Manage Orders",
        "2": "Manage Products",
        "0": "Exit"
    }
    print_menu("Main Menu", options)
    return get_input("Choose an option: ", options.keys())

def order_menu():
    options = {
        "1": "Create Order",
        "2": "Delete Order",
        "3": "List Orders",
        "4": "View Products in an Order",
        "5": "Find Order by ID",
        "0": "Back"
    }
    print_menu("Order Menu", options)
    return get_input("Choose an option: ", options.keys())

def product_menu():
    options = {
        "1": "Create Product",
        "2": "Delete Product",
        "3": "List Products",
        "4": "Find Product by ID",
        "0": "Back"
    }
    print_menu("Product Menu", options)
    return get_input("Choose an option: ", options.keys())

def create_order():
    name = input("Enter customer name: ").strip()
    try:
        order = Order.create(name)
        print(f"Order created with ID {order.id}")
    except Exception as e:
        print(f"Error: {e}")

def delete_order():
    order_id = input("Enter order ID to delete: ").strip()
    order = Order.find_by_id(int(order_id))
    if order:
        order.delete()
        print("Order deleted.")
    else:
        print("Order not found.")

def list_orders():
    orders = Order.get_all()
    for order in orders:
        print(order)

def view_order_products():
    order_id = input("Enter order ID to view products: ").strip()
    order = Order.find_by_id(int(order_id))
    if order:
        for product in order.products:
            print(product)
    else:
        print("Order not found.")

def find_order_by_id():
    order_id = input("Enter order ID to find: ").strip()
    order = Order.find_by_id(int(order_id))
    if order:
        print(order)
    else:
        print("Order not found.")

def create_product():
    name = input("Enter product name: ").strip()
    order_id = input("Enter order ID for this product: ").strip()
    order = Order.find_by_id(int(order_id))
    if order:
        try:
            product = Product.create(name, order)
            print(f"Product created with ID {product.id}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Order not found.")

def delete_product():
    product_id = input("Enter product ID to delete: ").strip()
    product = Product.find_by_id(int(product_id))
    if product:
        product.delete()
        print("Product deleted.")
    else:
        print("Product not found.")

def list_products():
    products = Product.get_all()
    for product in products:
        print(product)

def find_product_by_id():
    product_id = input("Enter product ID to find: ").strip()
    product = Product.find_by_id(int(product_id))
    if product:
        print(product)
    else:
        print("Product not found.")

def run_order_menu():
    while True:
        choice = order_menu()
        if choice == "1":
            create_order()
        elif choice == "2":
            delete_order()
        elif choice == "3":
            list_orders()
        elif choice == "4":
            view_order_products()
        elif choice == "5":
            find_order_by_id()
        elif choice == "0":
            break

def run_product_menu():
    while True:
        choice = product_menu()
        if choice == "1":
            create_product()
        elif choice == "2":
            delete_product()
        elif choice == "3":
            list_products()
        elif choice == "4":
            find_product_by_id()
        elif choice == "0":
            break

def main():
    print("Welcome to the Order Management CLI!")
    while True:
        choice = main_menu()
        if choice == "1":
            run_order_menu()
        elif choice == "2":
            run_product_menu()
        elif choice == "0":
            print("Exiting. Thank you for using the CLI!")
            break

if __name__ == '__main__':
    main()
