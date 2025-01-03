« Python. Знакомство с консолью »

1. Посчитайте площадь и периметр квадрата, сторона которого равна 6.

a = 6 # Сторона квадрата

perimeter = 4 * a  # Расчёт периметра
area = a ** 2  # Расчёт площади

print('Периметр:', perimeter)
print('Площадь:', area)

2. Посчитайте площадь и периметр прямоугольника 5×7.
  
a = 5  # Сторона A
b = 7  # Сторона B

perimeter = ( a + b ) * 2  # Расчёт периметра
area =  a * b    # Расчёт площади

print('Периметр:', perimeter)
print('Площадь:', area)

3. Создайте код, который можно использовать для планирования личных финансов.
При создании программы опирайтесь на данные, описанные ниже.
Сколько денег тратит пользователь на ипотеку в год и сколько он накопит за год (накопления составят остаток от заработанной платы после оплаты ипотеки и расходов на жизнь), если:

заработная плата в месяц = 100 000 руб.,
расходы на ипотеку = 30% от заработной платы,
расходы на жизнь = 50% от заработной платы?


salary = 100000  # Заработная плата
percent_mortgage = 30  # Ипотека
percent_life = 50  # На жизнь

mortgage = salary * (percent_mortgage * 0.01) *12
result = (salary - (( percent_life + percent_mortgage ) * 0.01 * salary )) * 12

print('Ипотека:', mortgage)
print('Накопления:', result)
