#Используемые столбцы:

#credit.policy - 1, если клиент соответствует критериям выдачи кредита, 0 в противном случае.
#purpose - цель кредита (принимает значения "credit_card", "debt_consolidation", "educational", "home_improvement", "major_purchase", "small_business" и "all_other").
#int.rate - процентная ставка по кредиту.
#installment - ежемесячный платеж, причитающийся заемщику в случае финансирования кредита.
#log.annual.inc - натуральный логарифм годового дохода заемщика, представленного им самим.
#dti - отношение долга к доходу заемщика (сумма долга, деленная на годовой доход).
#fico - кредитный рейтинг FICO заемщика.
#days.with.cr.line - количество дней, в течение которых у заемщика была открыта кредитная линия.
#revol.bal - возобновляемый баланс заемщика (сумма, не выплаченная в конце платежного цикла по кредитной карте).
#revol.util - коэффициент использования возобновляемой кредитной линии заемщиком (сумма использованной кредитной линии по отношению к общему объему доступных кредитов).
#inq.last.6mths - количество запросов заемщика от кредиторов за последние 6 месяцев.
#delinq.2yrs - количество раз, когда заемщик просрочивал платеж более чем на 30 дней за последние 2 года.
#pub.rec - количество негативных публичных записей о заемщике (заявления о банкротстве, налоговые залоги или судебные решения).
#not.fully.paid - неполностью выплаченный кредит ранее.

# 1 Выведите первые 5 строк датасета.
# 2 Сколько в датасете строк и столбцов?
# 3 Есть ли в датасете пропуски?
# 4 Выведите все описательные статистики по переменным
# 5 Какая средняя процентная ставка по кредиту?
# 6 Сколько клиентов соответствует условиям выдачи кредита?
# 7 Как отличается средний логарифм годового дохода заемщиков, которые соответствует условиям выдача кредита и тех, кто не соответствует?
# 8 Какой медианный ежемесячный платеж?
# 9 Сколько уникальных значений у переменной not.fully.paid?
# 10 Сделайте столбец annual.inc для подсчета годового дохода (выполните обратное преобразование столбца log.annual.inc)
# 11 Сделайте группировку по двум переменным: credit.policy и not.fully.paid. Посчитайте для каждой группы количество клиентов, средний ежемесячный платеж, медианный ежемесячный платеж, средний годовой доход.
# 12 Выведите топ-10 клиентов по уровню дохода среди тех, кто не удовлетворяет критериям выдачи кредита.
# 13 Есть ли выбросы у переменной annual.inc? Выбросами считайте наблюдения, которые не лежает в границах  [Q1−1.5IQR,Q3+1.5IQR] , где  IQR  - межквартильный размах,  Q1  - 25 перцентиль,  Q3  - 75 перцентиль.
# 14 Постройте распределения переменных annual.inc и log.annual.inc

import pandas as pd

df = pd.read_csv('loan_data.csv')

#1
print(df.head())
#2
print(df.shape)
#3
print(df.isnull().sum())
#4
print(df.describe())
#5
print(df['int.rate'].mean())
#6
print(df[df['credit.policy'] == True].shape[0])
#7
print(df[df['credit.policy'] == True]['log.annual.inc'].mean())
print(df[df['credit.policy'] == False]['log.annual.inc'].mean())
#8
print(df['installment'].median())
#9
print(df['not.fully.paid'].nunique())