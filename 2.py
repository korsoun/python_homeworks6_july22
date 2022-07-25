def my_eval (str_polynom):
    def conv_to_list (str_polynom):
        list_polynom = []
        str_coef = ''
        # Разбиваем строку, складывая числа и знаки операций в специальный список.
        for i in range(len(str_polynom)):
            # Позволительно вводить отрицательные числа. Если первый элемент не число (скорей всего минус), то он пойдет в str_coef и будет в составе следующего за ним числа.
            if not str_polynom[i].isdigit() and i == 0:
                str_coef += str_polynom[i]
            if str_polynom[i].isdigit():
                str_coef += str_polynom[i]
            if not str_polynom[i].isdigit() and i!= 0:
                list_polynom.append(str_coef)
                str_coef = ''
                list_polynom.append(str_polynom[i])
            if (str_polynom[i].isdigit()) and (i == len(str_polynom) - 1):
                list_polynom.append(str_coef)
        while '' in list_polynom:
            i = list_polynom.index('')
            list_polynom.pop(i)
        return list_polynom


    return(conv_to_list(str_polynom))

print(my_eval('4*(3+6)'))