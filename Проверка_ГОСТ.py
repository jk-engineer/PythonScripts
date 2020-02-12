# Программа для проверки актуальности стандартов через сайт Техэксперт http://docs.cntd.ru/.
# Copyright (C) 2019 Evgeniy Ipatov

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


# Алгоритм работы:
# Пользователь создает в папке с программой текстовый файл с названиями стандартов (каждый стандарт в новой строке).
# Программа считывает названия стандартов из текстового файла и каждый из них проверяет на актуальность на сайте Техэксперт.


import os
import sys
import webbrowser
import WebScraper
from os import listdir
from os.path import isfile, join


# Получение текущей директории
current_directory = os.path.dirname(os.path.abspath(__file__))
# Получение имен файлов, имеющихся в текущей директории
file_names = [name for name in listdir(current_directory) if isfile(join(current_directory, name))]
# Выбор файлов с расширением txt
file_names = [name for name in file_names if os.path.splitext(name.lower())[1] == '.txt']
file_names.sort()

# Выход из программы при отсутствии файлов txt
if len(file_names) == 0:
    print('\nНе найдены файлы с расширением *.txt. Завершение работы программы')
    sys.exit()

# Выбор необходимого файла с названиями стандартов
print('Выберите файл, который содержит названия проверяемых стандартов (введите число). Для выбора всех файлов введите 0 (нуль):\n')
for index in range(1, len(file_names) + 1):
    print(str(index) + ' -> ' + str(file_names[index - 1]))
print()
file_number = int(input())
file_list = []
if file_number == 0:
    file_list = file_names
elif file_number > (len(file_names)):
    while file_number > (len(file_names)):
        file_number = int(input('Ошибка. Повторите ввод числа:\n'))
    file_list = [file_names[file_number - 1]]
else:
    file_list = [file_names[file_number - 1]]

# Считывание названий стандартов из файлов
standard_names = []
for name in file_list:
    in_stream = open(name, 'rt', encoding='utf-8')
    for line in in_stream:
        # Замена повторных пробелов и знаков табуляции на один пробел
        line = (' '.join(line.split()))
        standard_names.append(line)
    in_stream.close()

# Поиск стандартов на сайте Техэксперт
print('Проверка стандартов...\n')
ws = WebScraper.WebScraper()
main_url = 'http://docs.cntd.ru'
search_url = main_url + '/search/intellectual?q='
failed_names = []
check_need_links = []

checked_count = 0
for name in standard_names:
    request_url = search_url + name
    parsed_page_search_results = ws.page_parser(request_url)
    document_links = []
    for element in parsed_page_search_results.find_all('a'):
        if str(element.get('href')).count('/document/') > 0 and str(element.get('title')) == '':
            document_links.append(str(element.get('href')))
    checked_count += 1
    print('Проверено: ' + str(checked_count) + ' из ' + str(len(standard_names)))
    # Документы, которые не удалось найти
    if len(document_links) == 0:
        failed_names.append(name)
        continue
    for link in document_links:
        parsed_page = ws.page_parser(main_url + link)
        # Поиск статуса стандарта на его странице по ключевому слову "Действующий"
        status_data = list(ws.get_attribute_values_by_element_value(parsed_page, 'span', 'class', 'Действующий'))
        if len(status_data) == 0:
            check_need_links.append(main_url + link)

# Отчет о завершении работы
print('\nПроверка завершена')
if len(failed_names) != 0:
    print('Не удалось найти следующие стандарты:\n')
    print('\n'.join(failed_names))
if len(check_need_links) != 0:
    print('\nНайдены стандарты с неправильным статусом. Открыть их в браузере? (Y/N) (Д/Н)')
    answer = input().lower()
    if answer == 'y' or answer == 'д':
        for link in check_need_links:
            webbrowser.open_new_tab(link)
