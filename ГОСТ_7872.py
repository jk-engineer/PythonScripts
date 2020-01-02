# Данная программа создает список типоразмеров подшипников по ГОСТ 7872.
# http://docs.cntd.ru/document/1200012893
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


import WebScraper


def check_value(value: str) -> str:
    """Возвращает значение, очищенное от лишних символов

    :param value: проверяемое значение
    :return:
    """
    value = str(value)
    value = value.replace(' ', '')
    value = value.replace('\n', '')
    value = value.replace('*', '')
    value = value.replace('-', '')
    value = value.replace('/', '_')
    return value


data_file_name = 'gost_7872.html'

# Список идентификаторов таблиц
tables_id_1 = [
    'P0044',
    'P0048',
    'P004C',
    'P0050',
    'P0054'
]
tables_id_2 = [
    'P0058',
    'P005C',
    'P0060',
    'P0065'
]

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Чтение данных из файла
output_values = []
columns_count = 8
for id_value in tables_id_1:
    data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
    for index in range(2, len(data_values), columns_count):
        config_name = check_value(data_values[index])
        d_value = check_value(data_values[index + 1])
        D_value = check_value(data_values[index + 3])
        d1_value = d_value
        D1_value = check_value(data_values[index + 2])
        H_value = check_value(data_values[index + 4])
        r_value = check_value(data_values[index + 5])
        mass_value = check_value(data_values[index + 7])
        output_values.append('\t'.join([config_name, d_value, d1_value, D_value, D1_value, H_value, r_value, r_value, mass_value]))

columns_count = 9
for id_value in tables_id_2:
    data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
    for index in range(2, len(data_values), columns_count):
        config_name = check_value(data_values[index])
        d_value = check_value(data_values[index + 1])
        D_value = check_value(data_values[index + 2])
        d1_value = check_value(data_values[index + 3])
        D1_value = check_value(data_values[index + 4])
        H_value = check_value(data_values[index + 5])
        r_value = check_value(data_values[index + 6])
        mass_value = check_value(data_values[index + 8])
        if mass_value == '':
            mass_value = '0'
        output_values.append('\t'.join([config_name, d_value, d1_value, D_value, D1_value, H_value, r_value, r_value, mass_value]))

# Запись данных в файл
with open('ГОСТ 7872 Подшипники.txt', 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values))
