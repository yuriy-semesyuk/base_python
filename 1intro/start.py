from math import sqrt


def task1():
    user_input = input('Введіть число')
    print('Number {} {}'.format(user_input, "!"))
    user_input = int(user_input)
    if user_input % 2 == 0:
        print('Parne')
    else:
        print('Neparne')


def task2():
    user_input = input("Скільки вам років")
    print('Number {} {}'.format(user_input, "!"))
    user_input = int(user_input)
    if user_input >= 18:
        print('Прохотьте')
    else:
        print('Ви не можите пройти тому що ви не є повнолітні')


def task3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for i in a:
        if i < 5:
            print(i)


def task4():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = b * b - 4 * a * c
    if d < 0:
        print("Розвязків немає")
    elif d == 0:
        x = -b / 2 * a
        print("x1= {}, x2 = {}".format(x, x))
    else:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        print("x1= {}, x2 = {}".format(x1, x2))


def task7():
    num = int(input("Введіть число\n"))
    sum = 0
    for n in range(num):
        sum += n
        print(n)
    print ("Результат = {}".format(sum))


def tack8():
    a = int(input("Введіть число 1\n"))
    b = int(input("Введіть число 2\n"))
    c = int(input("Введіть число 3\n"))
    if a == b or b == c or a == c:
        print("Результат = 0")
    else:
        sum = a + b + c
        print("Результат = {}".format(sum))


def task9():
    number_list = [3, 43, 12, 4, 56, 4, 234, 35, 56, 4]
    y = 0
    for i in number_list:
        if i == 4:
            y += 1
    print(y)


def tack10():
    r = 6
    v = 4 / 3 * 3.14 * (r ** 3)
    print(v)


def task11():
    n = int(input("Введіть число 1\n"))
    number = n + n * n + n * n * n
    print(n ** n)
    print("Ваше число {}".format(number))


if __name__ == "__main__":
    task9()
