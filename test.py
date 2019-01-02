from random import randint

"""
Напишіть декоратор ( функцію logg), яка обертає функції. Суть декоратора
в тому, що він логує (записує у файл) позиційні і ключова аргументи.
 кінці враппера записати у файл ‘Arguments are written’.  Також створити
 дві функції add & multiply, які підповідно додають, перемножують позиційні аргументи.
 Обернути функції add & multiply декоратором logg і викликати їх через if __name__ == “__main__”.
 Перевірити лог файл чи декоратор спрацював.
"""
from datetime import datetime, timedelta
from time import sleep


cache = {}


def cached (*dec_args, **dec_kwargs):
    def wrapper(func):
        def inner(*args, **kwargs):
            import ipdb; ipdb.set_trace()
            if args not in cache or (datetime.now() - cache[args]["time"]) > timedelta(seconds=dec_kwargs["second"]):
                cache[args] = {"res":func(*args, **kwargs), 'time':datetime.now()}
            return cache[args]["res"]
        return inner
    return wrapper


@cached(second = 2)
def add(*args, **kwargs):
    print('Add is called', args)
    return sum(args)


def task5():
    li = []
    for i in range(1):
        li.append(randint(1, 100))
    print(li)
    for i in li:
        li.pop()
        print(li)


if __name__ == "__main__":
    add()
    add()
