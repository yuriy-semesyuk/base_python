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


def len_of_args(*args):
    return len(args)


def rand_of_el():
    return len_of_args(1, 1, 334, 2424) - len_of_args(1, 2)


def not_doubled(var_list):
    return list(set(var_list))


def task6():
    print(not_doubled([12, "yu", 212, "yu", "yuriy", "yu", 43, 212, "yu", 212, 13]))


def palindrom(x):
    if not x:
        return True
    elif x[0] == x[-1]:
        return palindrom(x[1:-1])
    else:
        return False


def task7():
    res = palindrom("qwerewq")
    print(res)


def task8():
    var_list = []
    var_list_2 = []
    for i in range(5):
        for x in range(5):
            var_list.append(randint(1, 100))
        var_list_2.append(var_list)
        var_list = []
    for i in var_list_2:
        print(sorted(i))


def task9(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string


"""
def task10():
    count = int(input("Введіть кількість слів:\n"))
    sum_l = 0
    words = []
    for i in range(count):
        words.append(input())
    for i in words:
        sum_l += len(i)
    if sum_l < 10**5:
        print("ok")


def task10_1():
    count = int(input("Введіть кількість слів:\n"))
    words_list = []
    for i in range(count):
        name = input("Введіть {} слово:\n".format(i+1))
        for x in words_list:
            if x[0] == name:
                x[1] += 1
            else:
                words_list.append([name, 1])
            break
        if len(words_list) == 0:
            words_list.append([name, 1])
    n = ""
    for i in words_list:
        n += str(i[1]) + " "
    print(len(words_list))
    print(n)


def task11():
    count = int(input())
    all_words = []
    if 1 < count < 10**5:
        words_list = []
        for i in range(count):
            word = input()
            all_words.append(word)
        if len("".join(all_words)) < 10**6:
            print(len("".join(all_words)))
            for word in all_words:
                for x in words_list:
                    if word in x:
                        x[1] += 1
                words_list.append([word, 1])
                if len(words_list) == 0:
                    words_list.append([word, 1])
            res = ""
            for i in words_list:
                res += str(i[1]) + " "
            print(len(words_list))
            print(res)


def res(x):
    list_start = x
    list_finish = []
    count = 0
    while len(list_start):
        var = list_start[0]
        while var in list_start:
            count += 1
            list_start.remove(var)
        list_finish.append(str(count))
        count = 0
    result = " ".join(list_finish)
    print(len(list_finish))
    print(result)


def task12(list_words):
    list_join = "".join(list_words)
    if len(list_join) < 10**6 and list_join.isalpha() and list_join.islower():
        return True
    else:
        return False


def task13():
    count = int(input())
    all_words = []
    x = len(set(all_words))
    for _ in range(count):
        all_words.append(input())
    list_finish = ''
    count = 0
    while len(all_words):
        var = all_words[0]
        while var in all_words:
            count += 1
            all_words.remove(var)
        list_finish += str(count)
        count = 0
    print(x)
    print(list_finish)
"""


def task10_1():
    count = int(input())
    result_dict = {}
    result = ""
    for i in range(count):
        word = input()
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    for i in result_dict:
        result += "{}{}".format(str(result_dict[i]), " ")
    print("{}\n{}".format(len(result_dict), result))


def task10_2():
    count = int(input())
    if 1 <= count <= 10 ** 5:
        result_dict = {}
        all_list = ""
        result = ""
        for i in range(count):
            word = input()
            if word in result_dict:
                result_dict[word] += 1
            else:
                result_dict[word] = 1
            all_list += word
        if len(all_list) < 10**6 and all_list.isalpha() and all_list.islower():
            for i in result_dict:
                result += "{}{}".format(str(result_dict[i]), " ")
            print("{}\n{}".format(len(result_dict), result))


def task11():
    x1 = set()
    x2 = set()
    while len(x1) < 10:
        x1.add(randint(30, 50))
    while len(x2) < 10:
        x2.add(randint(30, 50))
    print(x1-x2)


if __name__ == "__main__":
    task11()
