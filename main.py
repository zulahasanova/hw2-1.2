
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


n = input("введите число монеток")
orel = input("введите число")
reshka = input("введите число")
min = 0
if orel < n:
        min = orel
else: 
    min = reshka
print(min)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


s = int(input("введите сумму чисел"))
p = int(input("введите произведение"))
x = 0
y = 0

if x <= 1000:
    x = s / 2
if y <= 1000:
    y = p / a
print(f'первое число ="{int(x)}", второе число ="{int(y)}"')


#for
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'первое число ="{x}", второе число ="{y}"')





# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

n = int(input("введите число: "))
i = 1
while i <= n:
    print(i)
    i = i * 2

