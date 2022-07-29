# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
num = int(input('Введите Num: '))
dictio = zip([i for i in range(1, num+1)], map(lambda i: 3*i+1, [i for i in range(1, num+1)])) 
print(dict(dictio))


