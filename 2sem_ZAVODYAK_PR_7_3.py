class Order:

    def __init__(self, number, info):

        self.number = number
        self.surname = info["surname"]
        self.product = info["product"]
        self.quantity = info["quantity"]
        self.price = info["price"]
        self.date = info["date"]

    def show(self):
        print(self.number, self.surname, self.product, self.quantity, self.price, self.date)


class OrderList:

    def __init__(self):

        self.orders = {}

    def add(self, order):

        self.orders[order.number] = order

    def remove(self, number):

        del self.orders[number]

    def search(self, key, value):

        result = []

        for order in self.orders.values():

            if getattr(order, key) == value:

                result.append(order)

        return result


o1 = Order(1, {"surname": "Ivanov", "product": "Phone", "quantity": 1, "price": 1000, "date": "26.02.2026"})

orders = OrderList()

orders.add(o1)

for o in orders.search("surname", "Ivanov"):
    o.show()