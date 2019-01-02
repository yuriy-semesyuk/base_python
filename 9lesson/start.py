from shop import Shop, Discount

if __name__ == "__main__":
    store = Shop("Ashan", "short")
    # store_1 = Shop("CA", "vest")
    # store_2 = Shop("mma", "ti")
    # store_3 = Shop("3mma", "#ti")
    store.discribe_shop()
    # store_1.discribe_shop()
    # store_2.discribe_shop()
    # store_3.discribe_shop()
    # print(store_3.numbe_for_unist)
    # store_3.numbe_for_unist = 3
    # print(store_3.numbe_for_unist)
    # store.set_nubers_of_units(5)
    # print(store.number_for_unist)
    # store.increment_number_of_units(5)
    # print(store.number_for_unist)
    store_discount = Discount("ew", "weq")
    store_discount.get_discount_products()
    store_discount.discount_products = ['90']
    store_discount.get_discount_products()
