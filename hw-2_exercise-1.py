# Напишите генератор, который принимает коллекцию с вложенными итерируемыми объектами, 
# а возвращает каждый элемент последовательно.Если "распаковать" все 
# получаемые значения в list, получится "сплющенный" список. Например:

# [[1, 2, 3], [4, [5, 6, [7, 8]]]] -> [1, 2, 3, 4, 5, 6, 7, 8]
# 
# Еще пример: [1, 2, 'abc', [2, 4], {'key' : 'value'}]
# 
# -> [1, 2, 'a', 'b', 'c', 2, 4, 'k', 'e', 'y']
# 
# (Итерация в словарях происходит по ключам)
# 
# Подсказка. Для проверки, что объект является итерируемым, можно использовать
# 
# from collections.abc import Iterable
# ...
# 
# if isinstance(x, Iterable):
# Функция isinstance(x, tp) проверяет, относится ли x к типу tp

from collections.abc import Iterable

def getUnpackingArray(array):
    for element in array:
        if isinstance(element, Iterable) and len(element) != 0:
            # Было бы красивее текст выводить целиком, а не посимвольно, но противоречит задаче. Я бы сделал выше isinstance(element, Iterable) and not isinstance(element, str)
            # и без if ниже, только yield from getUnpackingArray(element)
            if isinstance(element, str) and len(element) == 1:
                yield element
            else:
                yield from getUnpackingArray(element)
            # А ниже not isinstance(element, Iterable) or isinstance(element, str)
        elif not isinstance(element, Iterable):
            yield element

# Функция, печатющая результат для тестов (файл ../tests_hw-2_exercise-1.txt), сгенерированных с помощью Chad GPT (url: https://ask.chadgpt.ru/)
def testing():
    with open('tests_hw-2_exercise-1.txt') as file:
        for line in file:
            exit_array = list()
            gen = getUnpackingArray(eval(line))
            for non_iterable in gen:
                exit_array.append(non_iterable)
            print(exit_array)

testing()