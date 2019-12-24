# Данная программа создает список типоразмеров подшипников по ГОСТ 3635.
# http://docs.cntd.ru/document/1200012731
# Copyright (C) 2019 Evgeniy Ipatov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
    return value


data_file_name = 'gost_3635.html'

# Список идентификаторов таблиц
tables_id = [
    'P004E',
    'P005B',
    'P0060',
    'P006E'
]

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Чтение данных из файла
output_values = []
for id_value in tables_id:
    if id_value == 'P005B':
        columns_count = 14
        start_index = 17
    else:
        columns_count = 16
        start_index = 20
    data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
    for index in range(start_index, len(data_values), columns_count):
        config_name_1 = check_value(data_values[index])
        config_name_2 = check_value(data_values[index + 1])
        config_name_3 = check_value(data_values[index + 2])
        config_name_4 = check_value(data_values[index + 3])
        d_value = check_value(data_values[index + 4])
        D_value = check_value(data_values[index + 5])
        if D_value == '':
            D_value = 'none'
        B_value = check_value(data_values[index + 6])
        if B_value == '':
            B_value = 'none'
        C_value = check_value(data_values[index + 7])
        if C_value == '':
            C_value = 'none'
        d1_value = check_value(data_values[index + 8])
        if d1_value == '':
            d1_value = 'none'
        d2_value = check_value(data_values[index + 9])
        if d2_value == '':
            d2_value = 'none'
        r_value = check_value(data_values[index + 10])
        if r_value == '':
            r_value = 'none'
        r1_value = check_value(data_values[index + 11])
        if r1_value == '':
            r1_value = 'none'
        mass_value = check_value(data_values[index + 13])
        if mass_value == '':
            mass_value = 'none'
        for name in [config_name_1, config_name_2, config_name_3, config_name_4]:
            output_values.append('\t'.join([name, d_value, D_value, B_value, C_value, d1_value, d2_value, r_value, r1_value, mass_value]))

# Запись данных в файл
with open('ГОСТ 3635 Подшипники.txt', 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values))
