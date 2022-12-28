# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9


import random


def RandomArray(number: int) -> list:
    resultList = []
    for _ in range(number):
        randomNum = random.randint(1, number)
        resultList.append(randomNum)
    return resultList


#taskList = [4, 2, 3, 1]


def BlueberriesMax(array: list) -> int:
    maximum = 0
    for i in range(len(array)):
        harvest = array[i] + array[i-1] + array[i-2]
        if harvest > maximum:
            maximum = harvest
    return maximum


while True:
    try:
        beds = int(input('enter the number of beds: '))
        taskList = RandomArray(beds)

        print(f'the number of blueberries in the beds: {taskList}')

        maximumYield = BlueberriesMax(taskList)

        print(f'maximum yield from three beds: {maximumYield}')
        break

    except:
        print('Oops! Incorrect input. Try again..')
