# Данная программа создает список типоразмеров манжет по ГОСТ 8752.
# http://docs.cntd.ru/document/1200017919
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

# Для корректной работы требуется:
#   Python версии 3.x
#   Установленные пакеты BeautifulSoup4, requests


import WebScraper
import CheckNumber as chNum


def check_value(old_values, new_values):
    """Возвращает список проверенных значений

    :param old_values: список старых значений
    :param new_values: список новых значений
    :return:
    """
    checked_values = list(old_values)
    new_values = list(new_values)
    cur_value = ''
    for check_index in range(0, len(checked_values)):
        cur_value = str(new_values[check_index]).replace(' ', '')
        if chNum.is_number(cur_value):
            checked_values[check_index] = cur_value
        elif cur_value == '-':
            checked_values[check_index] = 'none'
    return checked_values


data_file_name = 'ГОСТ 8752-79.html'
# Идентификатор таблицы с размерами манжет
table_id = 'P0033'
columns_count = 9

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))

# Список диаметров начинается со значения 6 мм, поэтому необходимо найти индекс соответствующего элемента
start_index = data_values.index('6')
d_shaft = ''
D_row1 = ''
D_row2 = ''
D_row3 = ''
D_row4 = ''
h_row12 = ''
h_row3 = ''
h_row4 = ''
h1 = ''
output_values = []

for index in range(start_index, len(data_values), columns_count):
    d_shaft, D_row1, D_row2, D_row3, D_row4, h_row12, h_row3, h_row4, h1 = check_value([d_shaft, D_row1, D_row2, D_row3, D_row4, h_row12, h_row3, h_row4, h1],
                                                                                       data_values[index:index + columns_count])
    if D_row1 == 'none' or h_row12 == 'none':
        continue
    output_values.append('\t'.join(['x'.join([d_shaft, D_row1, h_row12]), d_shaft, D_row1, h_row12]))

# Запись данных в файл
with open('ГОСТ 8752-79 Манжеты.txt', 'w', encoding='utf-8') as fout:
    fout.write('\n'.join(output_values))
