"""
Реалізувати програму, в якій кожен з алгоритмів сортування оформити як окрему
функцію. Проілюструвати механізм використання параметрів різних типів. Забезпечити
підрахунок числа необхідних порівнянь, числа обмінів і часу роботи кожної функції,
сформувавши функції оцінки ефективності методів сортування. Підготувати єдині для
всіх алгоритмів тестові вихідні дані:
Barbak Vladuslav 122V
"""
import numpy as np
import random
import timeit  # Імпортуємо модуль для підрахунку часу
while True:
    vvod = input("Як будемо вводити?\nЯкщо рандомно-1, якщо з клавіатури - Будь-яка кнопка ")  # Вибераємо занчення для нашої змінної
    metod = input("Яким методом?" "\nБульбашковим-1, Вибором-2, Вставкою - Будь-яка кнопка ")
    sort = input("Як сортувати?\nЯкщо за зростанням-1, Якщо по спаданню - Будь-яка кнопка ")


    def bubl_up(s):  # Заводимо функцію для бульбашкового методу,для сортування по зростанню,де s-це кількість елементів
        global count_bubl  # Заводимо 2 лічильника і робимо їх глобальними що б їх можна було викликати в подальшому в функції оцінки роботи
        global obmin_bubl
        count_bubl = 0
        obmin_bubl = 0
        for i in range(1, n):  # Бульбашковий алгоритм за зростанням
            for j in range(n - 1, i - 1, -1):
                count_bubl += 1
                if (A[j - 1] > A[j]):
                    obmin_bubl += 1
                    A[j], A[j - 1] = A[j - 1], A[j]
        print(A)


    def bubl_down(s):  # Функція для бульбашкового алгоритму за спаданням
        global count_bubl
        global obmin_bubl
        count_bubl = 0
        obmin_bubl = 0
        for i in range(1, n):  # Бульбашковий алгоритм за спаданням
            for j in range(n - 1, i - 1, -1):
                count_bubl += 1
                if (A[j - 1] < A[j]):
                    obmin_bubl += 1
                    A[j], A[j - 1] = A[j - 1], A[j]
        print(A)


    def select_up(s):  # Функція для сортування вибором за зростанням
        global count_se
        global obmin_se
        count_se = 0
        obmin_se = 0
        for i in range(n - 1):  # Алгоритм сортування вибором за зростанням
            min = i
            for j in range(i + 1, n):
                count_se += 1
                if A[j] < A[min]:
                    obmin_se += 1
                    min = j
            A[i], A[min] = A[min], A[i]
        print(A)


    def select_down(s):  # Функція для сортування вибором за спаданням
        global count_se
        global obmin_se
        count_se = 0
        obmin_se = 0
        for i in range(n - 1):  # Алгоритм сортування вибором за спаданням
            min = i
            for j in range(i + 1, n):
                count_se += 1
                if A[j] > A[min]:
                    obmin_se += 1
                    min = j
            A[i], A[min] = A[min], A[i]
        print(A)


    def insertion_up(s):  # Функція для сортування вставкою за зростанням
        global count_ins
        global obmin_ins
        count_ins = 0
        obmin_ins = 0
        for i in range(1, n):  # Алгоритм сортування вставкою за зростанням
            j = i - 1
            key = A[i]
            while j >= 0 and A[j] > key:
                count_ins += 2
                obmin_ins += 1
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = key
        print(A)


    def insertion_down(s):  # Функція для сортування вставкою за спаданням
        global count_ins
        global obmin_ins
        count_ins = 0
        obmin_ins = 0
        for i in range(1, n):  # Алгоритм сортування вставкою за спаданням
            j = i - 1
            key = A[i]
            while j >= 0 and A[j] < key:
                count_ins += 2
                obmin_ins += 1
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = key
        print(A)


    if vvod == '1':
        x = int(input("Введіть кількість цифр "))
        A = np.zeros(x, dtype=int)  # Створюємо масив, і заповнюємо його рандомних значеннями
        for i in range(x):
            A[i] = random.randint(0, 100000)
        print(A)
        n = len(A)
        s = x
    else:  # Якщо значення vvod != 1, то ми заповнюємо наш масив самі, до 30 значень
        x = int(input("Введіть кількість цифр "))
        while x > 30:
            x = int(input("Введіть кількість до 30 "))
        A = np.zeros(x, dtype=int)
        for i in range(x):
            A[i] = int(input("Введіть число"))
        print(A)
        n = len(A)
        s = x


    def xarakteristika_bubl(countner):  # Заводимо функції для оцінки роботи кожного з методів
        print("Кількість порівнянь бульбашкового методу", countner)
        print("Количество обменов пузырькового метода", obmin_bubl)
        t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)  # Присваевам t,значение времени за которое работал каждый алгоритм
        print("Програма виконувалася за", t)


    def xarakteristika_select(countner):
        print("Кількість порівнянь методу вибору", countner)
        print("Кількість обмінів методу вибору", obmin_se)
        t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
        print("Програма виконувалася за", t)


    def xarakteristika_ins(countner):
        print("Кількість порівнянь методу вставками", countner)
        print("Кількість обмінів методу вставками", obmin_ins)
        t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
        print("Програма виконувалася за", t)


    if metod == '1':  # В залежності від обраних значень виводимо наші функції
        if sort == '1':
            bubl_up(s)
            xarakteristika_bubl(countner=count_bubl)  # Counter є поіменнованим параметром функції
        else:
            bubl_down(s)
            xarakteristika_bubl(countner=count_bubl)
    elif metod == '2':
        if sort == '1':
            select_up(s)
            xarakteristika_select(countner=count_se)
        else:
            select_down(s)
            xarakteristika_select(countner=count_se)
    else:
        if sort == '1':
            insertion_up(s)
            xarakteristika_ins(countner=count_ins)
        else:
            insertion_down(s)
            xarakteristika_ins(countner=count_ins)
    result = input("Хотите продолжить? Если да - 1, Если нет - інше: ")  # зацикливаем нашу программу
    if result == '1':
        continue
    else:
        break