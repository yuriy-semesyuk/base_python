def task1():
    numbers = input("введіть чилло\n")
    list_numbers = numbers.split()
    result = 0
    for i in list_numbers:
        result += int(i)
    print(result)


def task2():
    dict_river = {"dnipro": "ukraina", "nil": "ehupet", "bug": "lviv"}
    for x in dict_river:
        print("The {} runs through {}.".format(x, dict_river[x]))


def task3():
    e2g = {"stork": "storch", "hawk": "falke", "woodpecker": "specht", "owl": "eule"}
    for i in e2g.items():
        print(i)
    print(e2g["owl"])
    e2g["1"] = "2"
    e2g["3"] = "4"
    for i in e2g.items():
        print(i)


def task4():
    inventory = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'],
                 'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
                 'pocket': ['seashell', 'strange berry', 'lint']}
    # import ipdb; ipdb.set_trace()
    for i in (sorted(inventory["backpack"])):
        print(i)
    for i in inventory.setdefault('backpack'):
        if i == 'dagger':
            inventory.setdefault('backpack').remove(i)
    inventory['gold'] = inventory['gold'] + 50


def task5():
    prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
    stocks = {"banana": 132, "apple": 1323, "orange": 2323, "pear": 1231}
    total = 0
    for i in prices:
        print("{}:{}$ - {} kilogram".format(i, prices[i], stocks[i]))
        total += prices[i] * stocks[i]
    print("TOTAL = {}$".format(total))


if __name__ == "__main__":
    task1()
