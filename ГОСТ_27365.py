# Данная программа создает список типоразмеров подшипников по ГОСТ 27365.
# http://docs.cntd.ru/document/1200013031
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
    value = value.replace('/', '_')
    return value


data_file_name = 'gost_27365.html'

# Список идентификаторов таблиц
tables_id = [
    'P0029',
    'P002C',
    'P0030',
    'P0034',
    'P0039',
    'P003D',
    'P0041',
    'P0045',
    'P0049',
    'P004D',
    'P0051'
]

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Чтение данных из файла
output_values = []
columns_count = 11
for id_value in tables_id:
    data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
    for index in range(3, len(data_values), columns_count):
        config_name = check_value(data_values[index])
        d_value = check_value(data_values[index + 1])
        D_value = check_value(data_values[index + 2])
        B_value = check_value(data_values[index + 3])
        C_value = check_value(data_values[index + 4])
        T_value = check_value(data_values[index + 5])
        E_value = check_value(data_values[index + 6])
        r1_value = check_value(data_values[index + 7])
        r2_value = check_value(data_values[index + 8])
        alpha_value = check_value(data_values[index + 9])
        mass_value = check_value(data_values[index + 10])
        output_values.append('\t'.join([config_name, d_value, D_value, B_value, C_value, T_value, E_value, r1_value, r2_value, alpha_value, mass_value]))

# Запись данных в файл
with open('ГОСТ 27365 Подшипники.txt', 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values))
