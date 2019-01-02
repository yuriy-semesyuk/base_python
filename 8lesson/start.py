from random import randint

""" Написати 2 функції add ( додає позиційні аргументи в циклі for і вертає результат)
і add_advance( яка додає позиційні аргументи використовуючи builtin функцію sum).
Написати декоратор deprecated_add, обгорнути функцію add.
У враппері натомість викликати функцію add_advanced замість add,
і друкувати користувачеві повідомлення, що add функція є deprecated.
Перевірити чи дійсно викликається функція add_advance. """


def logg(func):
    def inner(*args, **kwargs):
        with open('logg.txt', 'a') as logg_file:
            logg_file.write(str(args))
            logg_file.write(str(kwargs))
            result = func(*args, **kwargs)
            logg_file.write('Arguments are written')
            return result

    return inner


@logg
def multiply(*args, **kwargs):
    result = 1
    for x in args:
        result = result * x
    return result


@logg
def task1(a, b, c):
    print('inside task1')


""" Напишіть декоратор ( функцію logg),
яка обертає функції. Суть декоратора  в тому, що він логує
(записує у файл) позиційні і ключова аргументи. В кінці враппера записати у
файл ‘Arguments are written’.  Також створити дві функції add & multiply,
які підповідно додають, перемножують позиційні аргументи. Обернути функції
add & multiply декоратором logg і викликати їх через if __name__ == “__main__”.
Перевірити лог файл чи декоратор спрацював."""

cache = {}


def cached(func):
    def inner(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return inner


@cached
@logg
def add(*args, **kwargs):
    print('Add is called', args)
    return sum(args)


"""Скопіювати функцію add із попереднього прикладу.
Написати декоратор cached. Суть декоратора в кешуванні роботи функції add.
Тобто треба створити словник де ключами будуть аргументи ( позиційні )
а значенням буде результат виконання функції add. Відповідно декоратор
має перевіряти чи є дані в словнику(була вже викликана функція add із такими
аргументами)  і вернути результат. Програмно перевірити чи дані беруться із кешу
чи виконується функція add ?"""


def deprecated_add(func):
    def wrapper(*args, **kwargs):
        result = add_advance(*args, **kwargs)
        return result
    return wrapper


@deprecated_add
def add(*args, **kwargs):
    num = 0
    for i in args:
        num += i
    print("add")
    return num


def add_advance(*args, **kwargs):
    print("add_adv")
    return sum(args)


""" Напишіть функцію, яка генерує словник.
Де ключами є слова square, cubic, four, five. А значення будуть лямбда функції 
які приймають число як аргумент, а вертають піднесення до відповідного степеня.
У функції по черзі викликати лямбда функції із випадково згенерованим числом від 10 до 20."""


def task4():
    di = {"square": lambda x: x ** 2, "cubic": lambda x: x ** 3, "four": lambda x: x ** 4, "five": lambda x: x ** 5}
    for i in di:
        print(di[i](randint(10, 20)))


""" Написати функцію, яка генерує ( рандомно) список списків( 5 вкладених списків )
довжиною 5 елементів. Відсортувати 1 список по 4 елементу вкладених списків.
Вивести відсортований список на екран."""


def task5():
    li = []
    for i in range(5):
        li_2 = []
        li.append(li_2)
        for x in range(5):
            li_2.append(randint(1, 100))
    print(sorted(li, key=lambda x: x[3]))


""" Написати функцію( gen_random) яка генерує рандомне число від 1 до 10.
Якщо число = 1, то вернути його, якщо більше 1 то викликати помилку (ImportError).
Написати функцію run ( яка буде викликати функцію gen_random і друкувати результат. 
Створити декоратор retry, який буде 20 разів пробувати викликати функцію gen_random.
Якщо за 20 разів gen_random не вернув результат то вернути ‘NO RESULT’. Запустити програму. """


def retry(func):
    def wrapper():
        for i in range(20):
            try:
                res = func()
                return res
            except:
                continue
        print("NO RESULT")

    return wrapper


@retry
def gen_random():
    num = randint(1, 10)
    if num == 1:
        return num
    raise Exception()


def run():
    print(gen_random())


if __name__ == "__main__":
    add()
