import string


def task1():
    inp = input("Введіть строку\n")
    return print(inp[-1::-1])


def task2_3():
    inp = input("Введіть строку\n")
    cout = 1
    for i in inp:
        if i.isupper():
            cout += 1
    print(cout)


def task4():
    inp = input("Введіть строку\n")
    n = string.ascii_lowercase
    for i in n:
        if i in inp:
            continue
        else:
            return False
    return True


def task6():
    inp = input("Введіть строку\n")
    res = ""
    for i in inp:
        if i.isupper():
            res += i.lower()
        else:
            res += i.upper()
    print(res)


def task7():
    inp_line = input("Введіть строку\n")
    max_width = int(input("Введіть максимальну ширину строки\n"))
    cout = 0
    new_line = ""
    for i in inp_line:
        if cout == max_width:
            new_line += "\n"
            new_line += i
            print(1)
            cout = 1
        else:
            new_line += i
            cout += 1
            print(cout)
    print(new_line)


def task8():
    inp_line = input("Введіть строку\n")
    n = inp_line.split()
    new_line = ""
    for i in n:
        new_line += i
        new_line += " "
    print(new_line)


def task9():
    inp_line = input("Введіть строку\n")
    inp = input("Введіть строку\n")
    cout = 0
    while True:
        if inp_line.find(inp) != (-1):
            cout += 1
            inp_line = inp_line[inp_line.find(inp)+1:]
        else:
            break
    print(cout)


def task10():
    first_name = input("Ваше імя\n")
    last_name = input("Ваше прізваще\n")
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))


def task11():
    input_line = input("Введіть число\n")
    len_line = len(input_line)
    var = ""
    result_line = ""
    result = "NO"
    for i in range(int(len_line*0.5)):
        var += input_line[i]
        result_line += var
        x = result_line
        while len(result_line) < len_line:
            x = str(int(x) + 1)
            result_line += x
        if result_line == input_line:
            result = "YES"
            break
        else:
            result_line = ""
    print(result)


def task12():
    password = input("Введіть пароль\n")
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    numbers_bool = False
    lower_case_bool = False
    upper_case_bool = False
    special_characters_bool = False
    if len(password) < 6:
        print("Ви ввели менше шисто символів")
    else:
        for i in password:
            if i in numbers:
                numbers_bool = True
            if i in lower_case:
                lower_case_bool = True
            if i in upper_case:
                upper_case_bool = True
            if i in special_characters:
                special_characters_bool = True
    error_line = ""
    if not numbers_bool:
        error_line += "Добавте в пароль 0123456789,\n"
    if not lower_case_bool:
        error_line += "Добавте в пароль abcdefghijklmnopqrstuvwxyz,\n"
    if not upper_case_bool:
        error_line += "Добавте в пароль ABCDEFGHIJKLMNOPQRSTUVWXYZ,\n"
    if not special_characters_bool:
        error_line += "Добавте в пароль !@#$%^&*()-+,\n"
    if error_line:
        print(error_line)
    else:
        print("Ваш пароль {}".format(password))


if __name__ == "__main__":
    task9()
