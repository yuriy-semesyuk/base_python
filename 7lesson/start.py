from random import randint


def task1():
    with open("numbers.txt", 'wt') as numbres:
        for i in range(10):
            numbres.write(str(randint(1, 100))+"\n")
    with open("numbers.txt", 'r') as numbres:
        num_sum = 0
        for i in numbres.readlines():
            num_sum += int(i.strip())
        with open("sum_numbers.txt", 'wt') as numbre:
            numbre.write(str(num_sum))


def task2():
    with open("learning_python.txt", 'r') as new_file:
        for i in new_file.readlines():
            print(i)


def task3():
    with open("learning_python.txt", 'r') as new_file:
        for i in new_file.readlines():
            print(i.replace("Python", "C"))


def task4():
    with open("book.txt", 'r') as new_file:
        with open("formatted_text.txt.", "wt") as line_book:
            for i in new_file.readlines():
                line_book.write(i.replace("\n", " "))


def task5():
    with open("book_2.txt", 'r') as new_file:
        with open("chapters.txt", "wt") as line_book:
            for i in new_file.readlines():
                if i.startswith("CHAPTER"):
                    line_book.write(i)


def task6():
    with open("book_3.txt", 'r') as new_file:
        count_upper = 0
        count_lower = 0
        for i in new_file:
            for x in i:
                if x.isalpha():
                    if x.isupper():
                        count_upper += 1
                    if x.islower():
                        count_lower += 1
        one_percent = (count_lower + count_upper)/100
        print("Upper {}%\nLower {}%".format(round(count_upper/one_percent),
                                            round(count_lower/one_percent)))


if __name__ == "__main__":
    task6()
