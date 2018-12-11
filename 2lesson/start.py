def task1():
    a = int(input("Введіть перше число\n"))
    b = int(input("Введіть друге число\n"))
    num1 = a+b
    num2 = a-b
    num3 = a*b
    print("Сума 2 чисел = {}\n".format(num1))
    print("Різниця чисел = {}\n".format(num2))
    print("Добуток = {}\n".format(num3))


def task2():
    number = int(input("Введіть перше число\n"))
    if number % 2 != 0 and number < 21:
        print("weird")
    elif number >= 2 and number <= 5:
        print("not weird")
    elif number >= 6 and number <= 20:
        print("weird")
    else:
        print("not weird")


def task3():
    year = is_leap(int(input("Введіть рік\n")))
    if year:
        print ("Є високосним роком")
    else:
        print ("Не є високосним роком")


def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            year = True
            return year
        elif year % 100 == 0:
            year = False
            return year
    else:
        year = False
    return year

if __name__ == "__main__":
    task3()