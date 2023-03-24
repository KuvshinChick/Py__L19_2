#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os.path
import json
import click


def add_human(people, Name, Zodiac_sign, Birth):
    # Вернуть словарь
    people.append(
        {
            "name": Name,
            "zodiac_sign": Zodiac_sign,
            "birth": Birth
        }
    )
    return people


def display_people(people_list):
    if people_list:
        # Заголовок таблицы.
        line = (f'{"+" + "-" * 15 + "+" + "-" * 12 + "+"}'
                f'{"-" * 15 + "+"}')
        print(line)
        print(f"|{'Name' :^15}|{'Birth ' :^12}|{'Zodiac_sign ' :^15}|")
        print(line)

        # Вывести данные о всех людях.
        for idx, man in enumerate(people_list):
            print(
                f'|{man.get("name", "") :^15}'
                f'|{man.get("birth", "") :^12}'
                f'|{man.get("zodiac_sign", "") :^15}|'
            )
            print(line)
    else:
        print("Список пуст.")


def select_zz(people_list, zz):
    # Инициализировать счетчик.
    count = 0
    result = []

    # Таблица с людьми
    for p in people_list:
        if zz == p.get('zodiac_sign'):
            count += 1
            result.append(p)

    # Если счетчик равен 0, то люди не найдены.
    if count == 0:
        print("Люди с заданным ЗЗ не найдены")

    # Возвратить список выбранных людей.
    return result


def save_people(file_name, people_list):
    """
    Сохранить всех людей в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(people_list, fout, ensure_ascii=False, indent=4)


def load_people(file_name):
    """
    Загрузить всех людей из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


@click.command()
@click.argument('command')
@click.argument('filename')
# @click.option('--name', prompt='name?',
#               help='The person`s name')
# @click.option('--zodiac_sign', prompt='Enter zodiac_sign', help='The zodiac_sign')
# @click.option('--birth', prompt='Enter person`s birth', help='The birth')

@click.option('--name', help='The person`s name')
@click.option('--zodiac_sign', help='The zodiac_sign')
@click.option('--birth', help='The birth')
def main(command, filename):  # , name, zodiac_sign, birth):
    # Загрузить всех людей из файла, если файл существует.
    is_dirty = False
    if os.path.exists(filename):
        people = load_people(filename)
    else:
        people = []
    # Отобразить всех работников.
    if command == "display":
        display_people(people)


if __name__ == '__main__':
    main()
