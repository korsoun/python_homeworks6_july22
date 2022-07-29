# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Решить с использованием выражений с третьей лекции.
general_list = [1, 3, 8, 7, 5, 7, 2, 3, 4, 1, 6]    # 8, 5, 2, 4, 6
def isunique (element):
    count = 0
    for i in range(len(general_list)):
        if general_list[i] == element:
            count += 1
    return True if count == 1 else False
unique_list = list(filter(isunique, general_list))
print((unique_list)) # [8, 5, 2, 4, 6]  17 строк с кодом против 9