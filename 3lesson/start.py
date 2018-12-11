def task1():
    name = input("Надрукуйте ваше імя\n")
    age = int(input("Напишіть ваш вік\n"))
    for x in range(age):
        print(name)


def task2():
    guess = 6
    n = 0
    while n < 4:
        total = int(input("вкажіть число"))
        if total == guess:
            print("you win")
            break
        n += 1
        print("невідгадали")


def task3():
    name = ""
    while name != "Iron Man":
        name = input("Яка головна роль Тоні Старка?\n")


def task4():
    number = int(input("Введіть число\n"))
    if number < 5:
        raise Exception("Число менше 5")
    else:
        for x in range(number):
            num = x*x
            print(num)


def task5():
    number = input("Введіть число\n") + " "
    number_list = []
    num_for_list = ""
    for x in number:
        if x == " ":
            number_list.append(int(num_for_list))
            num_for_list = ""
        else:
            num_for_list += x
    print(min(number_list), max(number_list))


def task5_1():
    number = input("Введіть число\n")
    list_str = number.split()
    list_int = []
    for x in list_str:
        list_int.append(int(x))
    print(min(list_int), max(list_int))


def task6():
    num_1 = 2000
    num_2 = 3201
    list_num = []
    for x in range(num_1, num_2):
        if x % 5 != 0 and x % 7 == 0:
            list_num.append(x)
    print(list_num)


def task7():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    print(letters[3:6])


def task8():
    list_num = [5, 5, 5]
    num = 1
    for x in list_num:
        num = num * x
    print(num)


def task9():
    list_number = [0, 1, 2, 3, 4, 5]
    list_number_2 = []
    for n in range(len(list_number)):
        if n % 2 == 0:
            list_number_2.insert(n, list_number[n + 1])
        else:
            list_number_2.insert(n, list_number[n - 1])
    print(list_number_2)


def task10():
    list_number = [0, 1, 2, 3, 4, 5]
    list_number_2 = []
    for n in range(len(list_number)):
        list_number_2.append("element")
        list_number_2.append(list_number[n])
    print(list_number_2)


def task11():
    list_name = [["Yuriy", "Semesyuk", 21],
                 ["Ihor", "Matruk", 22],
                 ["Roman", "Soloviyov", 23],
                 ["Iruna", "Koran", 24]]
    n = 0
    while n <= 2:
        list_name_2 = sorted(list_name, key=lambda i: i[n])
        print(list_name_2)
        n += 1


def task12():
    list_name = ["Yuriy", "Semesyuk", 21,
                 "Ihor", "Matruk", 22,
                 "Roman", "Soloviyov", 23,
                 "Iruna", "Koran", 24]
    n = "Semesyuk"
    if n in list_name:
        print(True)
    else:
        print(False)


def task12_1():
    list_name = ["Yuriy", "Semesyuk", 21,
                 "Ihor", "Matruk", 22,
                 "Roman", "Soloviyov", 23,
                 "Iruna", "Koran", 24]
    n = "Semesyuk"
    for i in list_name:
        if i == n:
            print(True)


if __name__ == "__main__":
    task12_1()
