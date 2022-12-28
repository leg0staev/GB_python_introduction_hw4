# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

import random

def RandomArray(number: int) -> list:
    resultList = []
    for _ in range(number):
        randomNum = random.randint(1, number//2)
        resultList.append(randomNum)
    return resultList

def GetSet(array: list) -> set:
    resultSet = set(array)
    return resultSet

while True:
    try:
        n = int(input('enter the number of digits in first array: '))
        m = int(input('enter the number of digits in second array: '))

        taskListFirst = RandomArray(n)
        taskListSecond = RandomArray(m)

        print(f'first generated array -> {taskListFirst}\nsecond generated array -> {taskListSecond}')

        setFromFirstArray = GetSet(taskListFirst)
        setFromSecondArray = GetSet(taskListSecond)
        resultSet = setFromFirstArray & setFromSecondArray

        
        print('result:',*resultSet)
        break
    except:
        print('Oops! Invalid input. Try again..')

