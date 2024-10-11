# 3.1 (Вспоминаем, что такое numpy) (6 баллов)
# 
# 1.  (2.5 б.)
# 
# Создайте с помощью np.random.randint numpy массив из 20-ти рандомных чисел. (0.5 б.) Посчитайте с помощью методов numpy и выведите на экран:
# 
# среднее значение в массиве (0.5 б.)
# минимальное значение в массиве (0.5 б.)
# максимальное значение в массиве (0.5 б.)
# индекс минимального элемента в массиве (0.5 б.)
# 2.  (1.5 б.)Создайте два numpy массива: в первом должны быть четные числа от 2 до 14 включительно, а во втором — числа 7, 11, 17, 18, 23, 30, 45.
# 
# Сложите массивы и возведите элементы получившегося массива в квадрат
# Выведите все элементы из первого массива, которые стоят на тех местах, где элементы второго массива больше 12 и дают остаток 3 при делении на 5.
# Для первого массива найдите остатки от деления на 2, а для второго — на 3.
# 3.  (2 б.)
# 
# Сгенерируйте рандомный массив b размера 3x1.
# Сгенерируйте матрицу С размера 3x3.
# Решите систему Cx = b с помощью numpy.linalg.solve
# Подумайте/погуглите, в каком случае numpy.linalg.solve вернет ошибку LinAlgError. Воспроизведите этот случай.

import numpy as np

# 1

np_rand_array = np.random.randint(1, 1000, 20)
print(np.average(np_rand_array))
print(np.min(np_rand_array))
print(np.argmin(np_rand_array))

# 2

np_array_1 = np.arange(2, 15, 2)
np_array_2 = np.array([7, 11, 17, 18, 23, 30, 45])

print(np.power(np_array_1 + np_array_2, 2))
print(np_array_1[(np_array_2 > 12) & (np_array_2 % 5 == 3)])
print(np_array_1 % 2)
print(np_array_2 % 3)

# 3

matrix_b_3x1 = np.random.rand(3, 1)
matrix_c_3x3 = np.random.rand(3, 3)

print(matrix_b_3x1, matrix_c_3x3)

matrix_x = np.linalg.solve(matrix_c_3x3, matrix_b_3x1)

print(matrix_x)

# numpy.linalg.solve вернет ошибку LinAlgError, если не получается вернуть обратную матрицу. Пример (bx = C вместо Cx = b, где b - неквадратная):
# Я сначала перепутал местами C и b и получил такую ошибку, т.к. матрица b неквадратная и вычислить обратную numpy не смог

matrix_b_3x1 = np.random.rand(3, 1)
matrix_c_3x3 = np.random.rand(3, 3)

print(matrix_b_3x1, matrix_c_3x3)

matrix_x = np.linalg.solve(matrix_b_3x1, matrix_c_3x3)

print(matrix_x)

# Или так:

matrix_x = np.linalg.solve(matrix_b_3x1, [[2,1,3],[1,0,0],[3,0,0]])

print(matrix_x)