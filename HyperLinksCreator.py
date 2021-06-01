# Программа создания списка ссылок для файлов текущей директории
# Copyright (C) 2019 - 2021 Evgeniy Ipatov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import os
from os import listdir
from os.path import isfile, join


def create_hyperlinks_from_files(output_filename: str):
    """Создает файл, содержащий гиперссылки на все файлы (кроме данного модуля), содержащиеся в текущей директории.

    output_filename - имя файла, в который будут записаны гиперссылки.
    """
    # Получение текущей директории
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    # Получение имен файлов, имеющихся в текущей директории
    file_names = [name for name in listdir(cur_dir) if isfile(join(cur_dir, name)) and name.count('HyperLinks') == 0]
    # Формирование ссылок
    hyperlinks = ['<p><a href="' + name + '">' + name + '</a></p>' for name in file_names]
    # Запись ссылок в файл
    write_hyperlinks_to_file(output_filename, hyperlinks)


def create_hyperlinks_from_names(output_filename: str, file_names: list, link_names: list):
    """Создает файл, содержащий гиперссылки на указанные файлы.

    output_filename - имя файла, в который будут записаны гиперссылки;
    file_names - список имен файлов;
    link_names - список названий гиперссылок.
    """
    # Формирование ссылок
    hyperlinks = []
    file_names = list(file_names)
    link_names = list(link_names)
    for i in range(0, len(file_names)):
        hyperlinks.append('<p><a href="' + file_names[i] + '">' + link_names[i] + '</a></p>')
    # Запись ссылок в файл
    write_hyperlinks_to_file(output_filename, hyperlinks)


def write_hyperlinks_to_file(file_name: str, hyperlinks: list):
    """Записывает в файл список гиперссылок.

    file_name - имя файла, в который записываются гиперссылки;
    hyperlinks - список гиперссылок.
    """
    with open(str(file_name), 'w', encoding='utf-8') as fout:
        fout.write('\n'.join(list(hyperlinks)))
