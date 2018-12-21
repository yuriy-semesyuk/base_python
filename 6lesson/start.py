from random import randint


def task1():
    print(max_of_three(2, 3, 5))


def max_of_three(a, b, c):
    number_list = [a, b, c]
    return max(number_list)


def task2():
    list_str = ["dfdsf", "sddfghfhdhfdhfhfdfs", "fsfdgdfgfdfsdf", "fdfsdf"]
    print(random_from_list(list_str))


def random_from_list(list_str):
    max_len = ""
    for i in list_str:
        if len(max_len) < len(i):
            max_len = i
    return max_len, len(max_len)


def random10():
    num_random = randint(0, 10)
    return num_random


def summarizer():
    result = 0
    while result < 100:
        result += random10()
    print(result)


def task3():
    number = input("ВВедіть число\n")
    print(find_super(number))


def find_super(number):
    num = 0
    for i in number:
        num += int(i)
    if num < 10:
        return num
    else:
        return find_super(str(num))


"""
Написати функцію (len_of_args), яка приймає ключові та позиційні аргументи 
( вертає довжину позиційних елементів - len(args) ) . 
Також  написати функцію rand_of_el, яка двічі викликає функцію len_of_args
і вертає різницю результатів.  Викликати функцію rand_of_el і надрукувати результат
"""

"""
def len_of_args(*args, **kwargs):


def rand_of_el():
"""


def not_doubled(var_list):
    return list(set(var_list))


def task6():
    print(not_doubled([12, "yu", 212, "yu", "yuriy", "yu", 43, 212, "yu", 212, 13]))


if __name__ == "__main__":
    task6()
