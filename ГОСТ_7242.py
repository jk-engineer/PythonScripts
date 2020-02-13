# Данная программа создает список типоразмеров подшипников по ГОСТ 7242.
# http://docs.cntd.ru/document/1200012751
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
    return value


data_file_name = 'gost_7242.html'

# Список идентификаторов таблиц
tables_id = [
    'P001B',
    'P001F',
    'P0022',
    'P0027'
]

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Чтение данных из файла
output_values_1 = []
output_values_2 = []
columns_count = 7
for id_value in tables_id:
    data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
    for index in range(3, len(data_values), columns_count):
        config_name_1 = check_value(data_values[index])
        config_name_2 = check_value(data_values[index + 1])
        d_value = check_value(data_values[index + 2])
        D_value = check_value(data_values[index + 3])
        B_value = check_value(data_values[index + 4])
        r_value = check_value(data_values[index + 5])
        mass_value = check_value(data_values[index + 6])
        output_values_1.append('\t'.join([config_name_1, d_value, D_value, B_value, r_value, r_value, mass_value]))
        output_values_2.append('\t'.join([config_name_2, d_value, D_value, B_value, r_value, r_value, mass_value]))

# Запись данных в файлы
with open('ГОСТ 7242 Подшипники.txt', 'a', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values_1))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_2))
