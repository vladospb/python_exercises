#Сравните производительность операций умножения матриц с использованием библиотеки NumPy и 
#стандартных списков Python для матриц размером от 2x2 до 100x100.

#п.1 Сгенерируйте две матрицы A и B случайного размера от nxn, заполненные случайными целыми числами от 1 до 50. (1 балл)
#п.2 Используя библиотеку NumPy, выполните умножение матриц A и B. Измерьте время выполнения операции. (2 балла)
#п.3 Реализуйте функцию для умножения матриц с помощью стандартных списков Python. Измерьте время выполнения этой операции. (3 балла)
#п.4 Сделайте вышеперечисленные пункты для n=2,...100. (4 балла)
#п.5 Для какого-нибудь n проверьте, что результаты совпадают. (1 балл)
#п.6 (5 баллов):
#(Вариант 1) Для каждого n выведите на экран размеры матриц и время выполнения умножения для обеих реализаций.

#Я ВЫБРАЛ ЭТОТ!!! (Вариант 2, с визуализацией) Постройте график, где по оси X будет размер матрицы, 
#по оси Y - время выполнения операции. Постройте два графика (для numpy и для стандартных списков)

import numpy as np
import time

# Создаю матрицы (п.1)
def mkmatrix(n):
    return np.array(list(np.random.randint(0, 50, n) for i in range(n)))

# Измеряю время (пп.2,3)
def benchmark(func):
    def wrapper(*args, **kwargs):
        entry_time = time.time()
        result = func(*args, **kwargs)
        exit_time = time.time()
        return result, exit_time - entry_time
    return wrapper

# Умножаю матрицы с помощью NumPy (п.2) и применяю к функции декоратор, подсчитывающий время выполнения
@benchmark
def multiply_with_np(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

# Умножаю матрицы без NumPy (п.3) и применяю к функции декоратор, подсчитывающий время выполнения
@benchmark
def multiply_without_np(matrix_a, matrix_b):
    n = len(matrix_a)
    result_of_multiply_without_np = list()
    for i in range(n):
        result_of_multiply_without_np.append(list())
        for j in range(n):
            result_of_multiply_without_np[-1].append(sum([matrix_a[i][z] * matrix_b[z][j] for z in range(n)]))
    return result_of_multiply_without_np

# применяю операции умножения для размерностей от 2 до 100 (п.4)
def getResult(min_n = 2, max_n = 100, n_for_check = 44):
    for n in range(min_n, max_n + 1):
        matrix_a = mkmatrix(n)
        matrix_b = mkmatrix(n)
        time_with_NumPy.append(multiply_with_np(matrix_a, matrix_b)[1])
        time_without_NumPy.append(multiply_without_np(matrix_a.tolist(), matrix_b.tolist())[1])

        # проверяю, равны ли результаты для обеих реализаций (п.5)
        if n == n_for_check:
            print(f'Для матриц размером {n}x{n} умножение матриц с NumPy и без дали одинаковый результат' \
                if multiply_with_np(matrix_a, matrix_b)[0].tolist() == multiply_without_np(matrix_a, matrix_b)[0] \
                else 'Что-то пошло не так')

# Создаю списки для времени выполнения умножения от 2 до 100-мерных матриц
time_with_NumPy = list()
time_without_NumPy = list()

import matplotlib.pyplot as plt
    
getResult(n_for_check = np.random.randint(2, 100))

x = list(range(2, 100 + 1))
y1 = time_with_NumPy
y2 = time_without_NumPy

# строю графики (п.6) и получаю 16 баллов
plt.xlabel('Размерность матриц')
plt.ylabel('Время умножения матриц')
plt.plot(x, y1, label = 'С Numpy')
plt.plot(x, y2, label = 'Без Numpy')
plt.legend(fontsize=14)
plt.show()

# или нет...?