def my_eval (str_polynom):

    # Первая часть - принимает строку с выражением, выдает список из элементов.
    def conv_to_list (str_polynom):
        list_polynom = [] # Список элементов выражения.
        str_coef = '' 
        # Разбиваем строку, складывая числа, скобки и знаки операций в специальный список.
        for i in range(len(str_polynom)):
            # Позволительно вводить отрицательные числа. Если первый элемент обозначает минус при числе, то он пойдет в str_coef и будет в составе следующего за ним числа.
            if str_polynom[i] == '-' and i == 0:
                str_coef += str_polynom[i]
            # Набор числа.
            if str_polynom[i].isdigit():
                str_coef += str_polynom[i]
            # Если число кончается, и за ним следует нечисловой символ.
            if not str_polynom[i].isdigit() and i!= 0:
                list_polynom.append(str_coef)
                str_coef = ''
                list_polynom.append(str_polynom[i])
            # Если все еще идет набор числа, но текущий элемент последний.
            if (str_polynom[i].isdigit()) and (i == len(str_polynom) - 1):
                list_polynom.append(str_coef)
        # Ситуация, когда после нечислового элемента - знака операции открываются скобки, распознается условием на 14-й строке. Поэтому между знаком и скобкой появляется пустая строка.
        # Избавляемся от всех возможных пустых строк.
        while '' in list_polynom:
            i = list_polynom.index('')
            list_polynom.pop(i)
        return list_polynom

    # Вторая часть - принимает список элементов, выдает решение выражения в виде числа. Не поддерживает скобки.
    def list_solution (list_polynom):
        # В первую очередь смотрим наличие умножений или делений.
        if '*' in list_polynom or '/' in list_polynom:
            # Если есть и то, и другое, то выполняем операции в порядке появления. Т.е сперва то действие, чей индекс первого появления меньше.
            if '*' in list_polynom and '/' in list_polynom:
                index_mult = list_polynom.index('*')
                index_div = list_polynom.index('/')
                if index_mult < index_div:
                    list_polynom[index_mult-1] = float(list_polynom[index_mult-1]) * float(list_polynom[index_mult+1])
                    list_polynom.pop(index_mult+1)
                    list_polynom.pop(index_mult)
                else:
                    list_polynom[index_div-1] = float(list_polynom[index_div-1]) / float(list_polynom[index_div+1])
                    list_polynom.pop(index_div+1)
                    list_polynom.pop(index_div)
            # Если знаков деления уже нет, то последовательно выполняем оставшиеся умножения.
            if ('*' in list_polynom) and (not '/' in list_polynom):
                index_mult = list_polynom.index('*')
                list_polynom[index_mult-1] = float(list_polynom[index_mult-1]) * float(list_polynom[index_mult+1])
                list_polynom.pop(index_mult+1)
                list_polynom.pop(index_mult)
            # То же самое, если наоборот осталось только деление
            if ('/' in list_polynom) and (not '*' in list_polynom):
                index_div = list_polynom.index('/')
                list_polynom[index_div-1] = float(list_polynom[index_div-1]) / float(list_polynom[index_div+1])
                list_polynom.pop(index_div+1)
                list_polynom.pop(index_div)
        # Если с умножением и делением разобрались, и таких знаков больше нет, а цикл может выполняться, значит еще есть плюсы или минусы.
        if not '*' in list_polynom and not '/' in list_polynom:
            # Аналогично умножениям и делениям. Если есть и +, и -, будем выполнять то, что раньше.
            if ('+' in list_polynom) and ('-' in list_polynom):
                index_sum = list_polynom.index('+')
                index_deduct = list_polynom.index('-')
                if index_sum < index_deduct:
                    list_polynom[index_sum-1] = float(list_polynom[index_sum-1]) + float(list_polynom[index_sum+1])
                    list_polynom.pop(index_sum+1)
                    list_polynom.pop(index_sum)
                else:
                    list_polynom[index_deduct-1] = float(list_polynom[index_deduct-1]) - float(list_polynom[index_deduct+1])
                    list_polynom.pop(index_deduct+1)
                    list_polynom.pop(index_deduct)
            # Последовательное суммирование, если осталось только оно.
            if ('+' in list_polynom) and (not '-' in list_polynom):
                index_sum = list_polynom.index('+')
                list_polynom[index_sum-1] = float(list_polynom[index_sum-1]) + float(list_polynom[index_sum+1])
                list_polynom.pop(index_sum+1)
                list_polynom.pop(index_sum)
            # Последовательное вычитание, если осталось только оно
            if ('-' in list_polynom) and (not '+' in list_polynom):
                index_deduct = list_polynom.index('-')
                list_polynom[index_deduct-1] = float(list_polynom[index_deduct-1]) - float(list_polynom[index_deduct+1])
                list_polynom.pop(index_deduct+1)
                list_polynom.pop(index_deduct)
        return list_polynom[0]

    # Третья часть - принимает список элементов, включая скобки, выдает список элементов, в котором раскрыта 1 скобка.
    def remove_brackets (list_polynom):
        opening_brackets = []
        # Получаем список индексов, на которых находятся открывающие скобки.
        for i in range(len(list_polynom)):
            if list_polynom[i] == '(':
                opening_brackets.append(i)
        start_bracket = opening_brackets[len(opening_brackets)-1] # Хранит позицию открытия скобки, с которой предстоит работа.
        closing_brackets = []
        # Получаем список индексов, на которых хранятся закрывающие скобки, рассматривая элементы после последней открывающей скобки.
        for i in range(opening_brackets[len(opening_brackets)-1], len(list_polynom)):
            if list_polynom[i] == ')':
                closing_brackets.append(i)
        end_bracket = closing_brackets[0] # Хранит позицию закрытия скобки, с которой предстоит работать
        inner_list = []
        # Составление списка выражения, находящегося в скобке
        for i in range(start_bracket + 1, end_bracket):
            inner_list.append(list_polynom[i])
        # Находим значение выражения в скобке
        inner_solution = list_solution(inner_list)
        list_polynom[start_bracket] = inner_solution
        while end_bracket != start_bracket:
            list_polynom.pop(end_bracket)
            end_bracket -= 1
        return list_polynom

    # Получаем общий список для выражения.
    list_polynom = conv_to_list(str_polynom)
    # Применяем нужную функцию и раскрыаем скобки.
    if  '(' in list_polynom:
        while '(' in list_polynom:
            list_polynom = remove_brackets(list_polynom)
    # Если в строке не было скобок, или с ними справились, решение простого выражения.
    polynom_solution = list_solution(list_polynom)
    return polynom_solution

text = '4*((3+6)*2)-17/((14-12)*(6+1))'
print(f'Введено выражение {text}')
print(f'Решение выражения: {round(my_eval(text), 3)}')