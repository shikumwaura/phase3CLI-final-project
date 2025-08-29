from models import Order, Product

def seed_data():
    for product in Product.get_all():
        product.delete()
    for order in Order.get_all():
        order.delete()

    order1 = Order.create(customer_name="Alice Smith")
    order2 = Order.create(customer_name="Bob Johnson")

    Product.create(name="Widget A", order=order1)
    Product.create(name="Widget B", order=order1)
    Product.create(name="Gadget X", order=order2)
    Product.create(name="Gadget Y", order=order2)
    Product.create(name="Gadget Z", order=order2)

    print("Seed data created successfully!")

if __name__ == "__main__":
    seed_data()
