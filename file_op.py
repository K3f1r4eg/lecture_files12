from pprint import pprint
import os

def open_file():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            cook_book.update({line: []})
            k = int(file.readline().strip())
            for x in range(k):
                lst = file.readline().strip().split(' | ')
                dict = {'ingredient_name': lst[0], 'quantity': lst[1], 'measure': lst[2]}
                cook_book[line].append(dict)
            file.readline()
    return cook_book

#pprint(open_file())

def view_cook_book():
    for key, value in open_file().items():
        print(f'\n {key}')
        for dct in value:
            print(f"{dct['ingredient_name'] + ' - ' + dct['quantity'] + ' ' + dct['measure']}")


def view_shopping_list(s_l):
    print('\n Для приготовления этих блюд пондобится:\n')
    dish = 1
    for key, values in s_l.items():
        print(f"{dish}.{key} {values['quantity']} {values['measure']}")
        dish += 1

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for ingred in dishes:
        for ingr in open_file()[ingred]:
            name_ingr = ingr.pop('ingredient_name')
            ingr['quantity'] = int(ingr['quantity']) * int(person_count)
            if name_ingr in shopping_list:
                ingr['quantity'] += shopping_list[name_ingr]['quantity']
            shopping_list.update({name_ingr: ingr})
    view_shopping_list(shopping_list)


def input_ingredients():
    try:
        lst = list(input('Введите через запятую блюда которые хотите: ').split(', '))
        persons = int(input('Введите количество человек: '))
        get_shop_list_by_dishes(lst, persons)
    except Exception:
        print('Кажется Вы где-то ошиблись с вводом. Перепроверьте и введите заново.')


def program():
    print('\n\n Добро пожаловать в список рецептов!'.upper())
    print('\n\n Вам необходимо ввести номер действия:'
          '\n\n 1. Показать рецепты.'
          '\n 2. Ввод нужных рецептов и количества человек.'
          '\n 0. Выйти из программы.')
    while True:
        prog = str(input('\n -----------------------------------------------------------------------------------------'
                         '\n\n номер действия: '.upper()))
        if prog == '1':
            view_cook_book()
        elif prog == '2':
            input_ingredients()
            print('\n\n Вам необходимо ввести номер действия:'
                  '\n\n 1. Показать рецепты.'
                  '\n 2. Ввод нужных рецептов и количества человек.'
                  '\n 0. Выйти из программы.')
        elif prog == '0':
            break

if __name__ == '__main__':
    program()