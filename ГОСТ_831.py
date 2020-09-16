# Данная программа создает список типоразмеров подшипников по ГОСТ 831.
# http://docs.cntd.ru/document/1200012724
# Copyright (C) 2019 - 2020 Evgeniy Ipatov

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
    value = value.replace('/', '_')
    value = value.replace('-', '')
    return value


data_file_name = 'gost_831.html'

# Список идентификаторов таблиц
tables_id_1 = [
    'P002D',
    'P0031',
    'P0038'
]

table_id_2 = 'P0043'
table_id_3 = 'P004A'
table_id_4 = 'P004E'

# Состояния элементов в модели (погашен/не погашен)
supressed = 'ПОГАШЕН'
unsupressed = 'НЕ ПОГАШЕН'

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Чтение данных из файла
output_values_6000 = []
output_values_26000 = []
output_values_36000 = []
output_values_46000 = []
output_values_66000 = []
output_values_76000 = []
columns_count = 12
for id_value in tables_id_1:
    data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
    if id_value == 'P002D':
        start_index = 21
    else:
        start_index = 22
    for index in range(start_index, len(data_values), columns_count):
        config_name_6000 = check_value(data_values[index])
        config_name_36000 = check_value(data_values[index + 1])
        config_name_46000 = check_value(data_values[index + 2])
        d_value = check_value(data_values[index + 3])
        D_value = check_value(data_values[index + 4])
        B_value = check_value(data_values[index + 5])
        r_value = check_value(data_values[index + 7])
        r1_value = check_value(data_values[index + 9])
        mass_value = check_value(data_values[index + 11])
        if config_name_6000 != '':
            output_values_6000.append('\t'.join([config_name_6000, d_value, D_value, B_value, r_value, r_value, r_value, r1_value, mass_value, supressed, supressed, unsupressed]))
        if config_name_36000 != '':
            output_values_36000.append('\t'.join([config_name_36000, d_value, D_value, B_value, r_value, r_value, r_value, r1_value, mass_value, supressed, supressed, unsupressed]))
        if config_name_46000 != '':
            output_values_46000.append('\t'.join([config_name_46000, d_value, D_value, B_value, r_value, r_value, r_value, r1_value, mass_value, supressed, supressed, unsupressed]))

data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id_2))
columns_count = 13
for index in range(23, len(data_values), columns_count):
    config_name_26000 = check_value(data_values[index])
    config_name_36000 = check_value(data_values[index + 1])
    config_name_46000 = check_value(data_values[index + 2])
    config_name_66000 = check_value(data_values[index + 3])
    d_value = check_value(data_values[index + 4])
    D_value = check_value(data_values[index + 5])
    B_value = check_value(data_values[index + 6])
    r_value = check_value(data_values[index + 8])
    r1_value = check_value(data_values[index + 10])
    mass_value = check_value(data_values[index + 12])
    if config_name_26000 != '':
        output_values_26000.append('\t'.join([config_name_26000, d_value, D_value, B_value, r_value, r1_value, r1_value, r1_value, mass_value, unsupressed, unsupressed, supressed]))
    if config_name_36000 != '':
        output_values_36000.append('\t'.join([config_name_36000, d_value, D_value, B_value, r_value, r_value, r_value, r1_value, mass_value, supressed, supressed, unsupressed]))
    if config_name_46000 != '':
        output_values_46000.append('\t'.join([config_name_46000, d_value, D_value, B_value, r_value, r_value, r_value, r1_value, mass_value, supressed, supressed, unsupressed]))
    if config_name_66000 != '':
        output_values_66000.append('\t'.join([config_name_66000, d_value, D_value, B_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, supressed]))

data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id_3))
columns_count = 10
for index in range(2, len(data_values), columns_count):
    config_name_66000 = check_value(data_values[index])
    d_value = check_value(data_values[index + 1])
    D_value = check_value(data_values[index + 2])
    B_value = check_value(data_values[index + 3])
    r_value = check_value(data_values[index + 5])
    if r_value != '':
        r_backup = r_value
    r_value = r_backup
    r1_value = check_value(data_values[index + 7])
    if r1_value != '':
        r1_backup = r1_value
    r1_value = r1_backup
    mass_value = check_value(data_values[index + 9])
    output_values_66000.append('\t'.join([config_name_66000, d_value, D_value, B_value, r_value, r_value, r_value, r1_value, mass_value, supressed, supressed, unsupressed]))

data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id_4))
for index in range(2, len(data_values), columns_count):
    config_name_76000 = check_value(data_values[index])
    d_value = check_value(data_values[index + 1])
    D_value = check_value(data_values[index + 2])
    B_value = check_value(data_values[index + 3])
    if B_value != '':
        B_backup = B_value
    B_value = B_backup
    r_value = check_value(data_values[index + 5])
    if r_value != '':
        r_backup = r_value
    r_value = r_backup
    r1_value = check_value(data_values[index + 7])
    if r1_value != '':
        r1_backup = r1_value
    r1_value = r1_backup
    mass_value = check_value(data_values[index + 9])
    output_values_76000.append('\t'.join([config_name_76000, d_value, D_value, B_value, r_value, r1_value, r_value, r_value, mass_value, unsupressed, supressed, supressed]))

# Запись данных в файл
with open('ГОСТ 831 Подшипники.txt', 'a', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values_6000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_26000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_36000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_46000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_66000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_76000))
