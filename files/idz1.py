#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Используя замыкания функций, объявите внутреннюю функцию,
которая на основе двух параметров вычисляет площадь фигуры
Какой именно фигуры: треугольника или прямоугольника,
определяется параметром type внешней функции.
Если type принимает значение 0, то вычисляется площадь треугольника,
а иначе – прямоугольника.
По умолчанию параметр type должен быть равен 0.
Вычисленное значение должно возвращаться внутренней функцией.
Вызовите внутреннюю функцию замыкания и
отобразите на экране результат ее работы.
'''


def fun(opr):
    def culc(a, b):
        if opr == 0:
            return f'Площадь триуголника: {0.5 * a * b}'
        elif opr == 1:
            return f'Площадь прямоуголника: {a * b}'
        else:
            return "Ошибка"
    return culc


if __name__ == '__main__':
    print(fun(
            int(input('Вычислить площадь триуголника - 0, прямоугника - 1: ')))
            (float(input('Введите строкону 1: ')),
            float(input('Введите сторону 2: '))
            )
         )
