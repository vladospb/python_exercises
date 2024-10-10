#Вводится числа через пробел с одной строке. Затем вводится число n.
#
#Напишите программу, которая находит все уникальные пары чисел из списка, где сумма каждой пары равна числу n. Можете использовать itertools.
#
#Например, списка [1, 2, 3, 4, 5, 6] и n=7 программа должна вывести пары чисел, которые в сумме дают 7: [(1, 6), (2, 5), (3, 4)].
#
#Гарантируется, что числа в списке не повторяются.
#
#Пары в кортежах должны быть в том же порядке, что в исходном списке.

#from itertools import count

# Функция, возвращающая пары чисел, которые в сумме дают заданное в том же порядке, что в исходном списке
def mkListOfPairs(entry_array, sum):
    result = list()

    for i in range(len(entry_array)):
        for j in range(i + 1, len(entry_array)):
            if entry_array[i] + entry_array[j] == sum:
                result.append((entry_array[i], entry_array[j]))

    return result

# Проверяю на примере из задания
print((result := mkListOfPairs([1, 2, 3, 4, 5, 6], 7)) == [(1, 6), (2, 5), (3, 4)], result)

# Функция, проверяющая результат тестами (файл ../tests_hw-2_exercise-2.txt), сгенерированными с помощью Chad GPT (url: https://ask.chadgpt.ru/)
def testing():
    i = 0
    entry_arrays = list()
    sum_arrays = list()
    exit_arrays = list()
    with open('tests_hw-2_exercise-2.txt') as file:
        i = 0
        for line in file:
            if i % 4 == 0:
                entry_arrays.append(list(int(j) for j in line.strip().split()))
            elif i % 4 == 1:
                sum_arrays.append(int(line.strip()))
            elif i % 4 == 2:
                exit_arrays.append(line.strip())
            i += 1

    for i in range(len(entry_arrays)):
        print(str(mkListOfPairs(entry_arrays[i], sum_arrays[i])) == exit_arrays[i], mkListOfPairs(entry_arrays[i], sum_arrays[i]))

testing()
