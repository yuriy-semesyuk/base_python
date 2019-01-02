class Shop:
    number_for_unist = 0

    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type

    def discribe_shop(self):
        print("This is {} and {}".format(self.shop_name, self.store_type))

    def open_shop(self):
        print("is Open")

    def set_nubers_of_units(self, number_of_units):
        self.number_for_unist = number_of_units

    def increment_number_of_units(self, increment_number):
        self.number_for_unist += increment_number


class Discount(Shop):
    discount_products = []

    def get_discount_products(self):
        print(self.discount_products)


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"My name is {self.first_name} my last name is {self.last_name}")

    def greeting_user(self):
        print(f"Hello {self.first_name}")


if __name__ == "__main__":
    user = User("Yuriy", "Semesyuk", 25)
    user.describe_user()
    user.greeting_user()