# Данная программа создает список типоразмеров подшипников по ГОСТ 8328.
# http://docs.cntd.ru/document/1200012894
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


data_file_name = 'gost_8328.html'

# Список идентификаторов таблиц
table_1_id = 'P002A'
table_2_id = 'P0030'
table_3_id = 'P0036'
table_4_id = 'P003C'
table_5_id = 'P0042'
table_6_id = 'P0048'
table_7_id = 'P004E'

# Списки данных
output_values_2000 = []
output_values_12000 = []
output_values_32000 = []
output_values_42000 = []
output_values_52000 = []
output_values_62000 = []
output_values_92000 = []
output_values_102000 = []

# Состояния буртиков колец в модели (погашен/не погашен)
supressed = 'ПОГАШЕН'
unsupressed = 'НЕ ПОГАШЕН'

# Парсинг файла
ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Чтение данных из таблицы 1
table_id = table_1_id
columns_count = 10
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))
start_index = 12
for index in range(start_index, len(data_values), columns_count):
    config_name_2000 = check_value(data_values[index])
    config_name_32000 = check_value(data_values[index + 1])
    d_value = check_value(data_values[index + 2])
    D_value = check_value(data_values[index + 3])
    B_value = check_value(data_values[index + 4])
    if B_value != '':
        B_backup = B_value
    B_value = B_backup
    b_value = '5'
    r_value = check_value(data_values[index + 5])
    if r_value != '':
        r_backup = r_value
    r_value = r_backup
    r1_value = check_value(data_values[index + 7])
    if r1_value != '':
        r1_backup = r1_value
    r1_value = r1_backup
    mass_value = check_value(data_values[index + 9])
    if mass_value == '':
        mass_value = '0'
    output_values_2000.append('\t'.join([config_name_2000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, supressed]))
    output_values_32000.append('\t'.join([config_name_32000, d_value, D_value, B_value, b_value, r1_value, r1_value, r_value, r_value, mass_value, supressed, supressed, unsupressed, unsupressed, supressed, supressed]))

# Чтение данных из таблицы 2
table_id = table_2_id
columns_count = 10
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))
start_index = 12
for index in range(start_index, len(data_values), columns_count):
    config_name_2000 = check_value(data_values[index])
    config_name_32000 = check_value(data_values[index + 1])
    d_value = check_value(data_values[index + 2])
    D_value = check_value(data_values[index + 3])
    B_value = check_value(data_values[index + 4])
    if B_value != '':
        B_backup = B_value
    B_value = B_backup
    b_value = '5'
    r_value = check_value(data_values[index + 5])
    if r_value != '':
        r_backup = r_value
    r_value = r_backup
    r1_value = check_value(data_values[index + 7])
    if r1_value != '':
        r1_backup = r1_value
    r1_value = r1_backup
    mass_value = check_value(data_values[index + 9])
    if mass_value == '':
        mass_value = '0'
    output_values_2000.append('\t'.join([config_name_2000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, supressed]))
    output_values_32000.append('\t'.join([config_name_32000, d_value, D_value, B_value, b_value, r1_value, r1_value, r_value, r_value, mass_value, supressed, supressed, unsupressed, unsupressed, supressed, supressed]))

# Чтение данных из таблицы 3
table_id = table_3_id
columns_count = 14
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))
start_index = 16
for index in range(start_index, len(data_values), columns_count):
    config_name_2000 = check_value(data_values[index])
    config_name_12000 = check_value(data_values[index + 1])
    config_name_32000 = check_value(data_values[index + 2])
    config_name_42000 = check_value(data_values[index + 3])
    config_name_92000 = check_value(data_values[index + 4])
    config_name_102000 = check_value(data_values[index + 5])
    d_value = check_value(data_values[index + 6])
    D_value = check_value(data_values[index + 7])
    B_value = check_value(data_values[index + 8])
    if B_value != '':
        B_backup = B_value
    B_value = B_backup
    b_value = '5'
    r_value = check_value(data_values[index + 9])
    if r_value != '':
        r_backup = r_value
    r_value = r_backup
    r1_value = check_value(data_values[index + 11])
    if r1_value != '':
        r1_backup = r1_value
    r1_value = r1_backup
    mass_value = check_value(data_values[index + 13])
    if mass_value == '':
        mass_value = '0'
    output_values_2000.append('\t'.join([config_name_2000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, supressed]))
    if config_name_12000 != '':
        output_values_12000.append('\t'.join([config_name_12000, d_value, D_value, B_value, b_value, r_value, r_value, r_value, r1_value, mass_value, unsupressed, unsupressed, unsupressed, supressed, supressed, supressed]))
    output_values_32000.append('\t'.join([config_name_32000, d_value, D_value, B_value, b_value, r1_value, r1_value, r_value, r_value, mass_value, supressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    output_values_42000.append('\t'.join([config_name_42000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    output_values_92000.append('\t'.join([config_name_92000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, unsupressed, unsupressed, unsupressed, supressed, supressed]))
    if config_name_102000 != '':
        output_values_102000.append('\t'.join([config_name_102000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, unsupressed]))

# Чтение данных из таблицы 4
table_id = table_4_id
columns_count = 12
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))
start_index = 21
for index in range(start_index, len(data_values), columns_count):
    config_name_2000 = check_value(data_values[index])
    config_name_32000 = check_value(data_values[index + 1])
    config_name_42000 = check_value(data_values[index + 2])
    config_name_92000 = check_value(data_values[index + 3])
    d_value = check_value(data_values[index + 4])
    D_value = check_value(data_values[index + 5])
    B_value = check_value(data_values[index + 6])
    if B_value != '':
        B_backup = B_value
    B_value = B_backup
    b_value = '5'
    r_value = check_value(data_values[index + 7])
    if r_value != '':
        r_backup = r_value
    r_value = r_backup
    r1_value = check_value(data_values[index + 9])
    if r1_value != '':
        r1_backup = r1_value
    r1_value = r1_backup
    mass_value = check_value(data_values[index + 11])
    if mass_value == '':
        mass_value = '0'
    output_values_2000.append('\t'.join([config_name_2000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, supressed]))
    output_values_32000.append('\t'.join([config_name_32000, d_value, D_value, B_value, b_value, r1_value, r1_value, r_value, r_value, mass_value, supressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    output_values_42000.append('\t'.join([config_name_42000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    output_values_92000.append('\t'.join([config_name_92000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, unsupressed, unsupressed, unsupressed, supressed, supressed]))

# Чтение данных из таблицы 5
table_id = table_5_id
columns_count = 16
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))
start_index = 18
b_backup = ''
for index in range(start_index, len(data_values), columns_count):
    config_name_2000 = check_value(data_values[index])
    config_name_12000 = check_value(data_values[index + 1])
    config_name_32000 = check_value(data_values[index + 2])
    config_name_42000 = check_value(data_values[index + 3])
    config_name_62000 = check_value(data_values[index + 4])
    config_name_92000 = check_value(data_values[index + 5])
    config_name_102000 = check_value(data_values[index + 6])
    d_value = check_value(data_values[index + 7])
    D_value = check_value(data_values[index + 8])
    B_value = check_value(data_values[index + 9])
    if B_value != '':
        B_backup = B_value
    B_value = B_backup
    b_value = check_value(data_values[index + 10])
    if b_value != '':
        b_backup = b_value
    b_value = b_backup
    r_value = check_value(data_values[index + 11])
    if r_value != '':
        r_backup = r_value
    r_value = r_backup
    r1_value = check_value(data_values[index + 13])
    if r1_value != '':
        r1_backup = r1_value
    r1_value = r1_backup
    mass_value = check_value(data_values[index + 15])
    if mass_value == '':
        mass_value = '0'
    output_values_2000.append('\t'.join([config_name_2000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, supressed]))
    if config_name_12000 != '':
        output_values_12000.append('\t'.join([config_name_12000, d_value, D_value, B_value, b_value, r_value, r_value, r_value, r1_value, mass_value, unsupressed, unsupressed, unsupressed, supressed, supressed, supressed]))
    output_values_32000.append('\t'.join([config_name_32000, d_value, D_value, B_value, b_value, r1_value, r1_value, r_value, r_value, mass_value, supressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    output_values_42000.append('\t'.join([config_name_42000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    if config_name_62000 != '':
        output_values_62000.append('\t'.join([config_name_62000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, unsupressed, unsupressed, unsupressed, supressed]))
    output_values_92000.append('\t'.join([config_name_92000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, unsupressed, unsupressed, unsupressed, supressed, supressed]))
    if config_name_102000 != '':
        output_values_102000.append('\t'.join([config_name_102000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, unsupressed]))

# Чтение данных из таблицы 6
table_id = table_6_id
columns_count = 16
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))
start_index = 18
b_backup = ''
for index in range(start_index, len(data_values), columns_count):
    config_name_2000 = check_value(data_values[index])
    config_name_12000 = check_value(data_values[index + 1])
    config_name_32000 = check_value(data_values[index + 2])
    config_name_42000 = check_value(data_values[index + 3])
    config_name_52000 = check_value(data_values[index + 4])
    config_name_62000 = check_value(data_values[index + 5])
    config_name_92000 = check_value(data_values[index + 6])
    d_value = check_value(data_values[index + 7])
    D_value = check_value(data_values[index + 8])
    B_value = check_value(data_values[index + 9])
    if B_value != '':
        B_backup = B_value
    B_value = B_backup
    b_value = check_value(data_values[index + 10])
    if b_value != '':
        b_backup = b_value
    b_value = b_backup
    r_value = check_value(data_values[index + 11])
    if r_value != '':
        r_backup = r_value
    r_value = r_backup
    r1_value = check_value(data_values[index + 13])
    if r1_value != '':
        r1_backup = r1_value
    r1_value = r1_backup
    mass_value = check_value(data_values[index + 15])
    if mass_value == '':
        mass_value = '0'
    output_values_2000.append('\t'.join([config_name_2000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, supressed]))
    if config_name_12000 != '':
        output_values_12000.append('\t'.join([config_name_12000, d_value, D_value, B_value, b_value, r_value, r_value, r_value, r1_value, mass_value, unsupressed, unsupressed, unsupressed, supressed, supressed, supressed]))
    output_values_32000.append('\t'.join([config_name_32000, d_value, D_value, B_value, b_value, r1_value, r1_value, r_value, r_value, mass_value, supressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    output_values_42000.append('\t'.join([config_name_42000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    if config_name_52000 != '':
        output_values_52000.append('\t'.join([config_name_52000, d_value, D_value, B_value, b_value, r1_value, r1_value, r_value, r_value, mass_value, supressed, supressed, unsupressed, unsupressed, unsupressed, supressed]))
    if config_name_62000 != '':
        output_values_62000.append('\t'.join([config_name_62000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, unsupressed, unsupressed, unsupressed, supressed]))
    output_values_92000.append('\t'.join([config_name_92000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, unsupressed, unsupressed, unsupressed, supressed, supressed]))

# Чтение данных из таблицы 7
table_id = table_7_id
columns_count = 15
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))
start_index = 17
b_backup = ''
for index in range(start_index, len(data_values), columns_count):
    config_name_2000 = check_value(data_values[index])
    config_name_32000 = check_value(data_values[index + 1])
    config_name_42000 = check_value(data_values[index + 2])
    config_name_62000 = check_value(data_values[index + 3])
    config_name_92000 = check_value(data_values[index + 4])
    config_name_102000 = check_value(data_values[index + 5])
    d_value = check_value(data_values[index + 6])
    D_value = check_value(data_values[index + 7])
    B_value = check_value(data_values[index + 8])
    if B_value != '':
        B_backup = B_value
    B_value = B_backup
    b_value = check_value(data_values[index + 9])
    if b_value != '':
        b_backup = b_value
    b_value = b_backup
    r_value = check_value(data_values[index + 10])
    if r_value != '':
        r_backup = r_value
    r_value = r_backup
    r1_value = check_value(data_values[index + 12])
    if r1_value != '':
        r1_backup = r1_value
    r1_value = r1_backup
    mass_value = check_value(data_values[index + 14])
    if mass_value == '':
        mass_value = '0'
    output_values_2000.append('\t'.join([config_name_2000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, supressed]))
    output_values_32000.append('\t'.join([config_name_32000, d_value, D_value, B_value, b_value, r1_value, r1_value, r_value, r_value, mass_value, supressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    output_values_42000.append('\t'.join([config_name_42000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, unsupressed, unsupressed, supressed, supressed]))
    if config_name_62000 != '':
        output_values_62000.append('\t'.join([config_name_62000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, unsupressed, unsupressed, unsupressed, supressed]))
    output_values_92000.append('\t'.join([config_name_92000, d_value, D_value, B_value, b_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, unsupressed, unsupressed, unsupressed, supressed, supressed]))
    if config_name_102000 != '':
        output_values_102000.append('\t'.join([config_name_102000, d_value, D_value, B_value, b_value, r_value, r_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed, supressed, supressed, unsupressed]))

# Запись данных в файл
with open('ГОСТ 8328 Подшипники.txt', 'a', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values_2000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_12000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_32000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_42000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_52000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_62000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_92000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_102000))
