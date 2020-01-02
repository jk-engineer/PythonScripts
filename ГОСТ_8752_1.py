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


import WebScraper


def check_value(value: str) -> str:
    """Возвращает значение, очищенное от лишних символов

    :param value: проверяемое значение
    :return:
    """
    value = str(value)
    value = value.replace(' ', '')
    value = value.replace('\n', '')
    return value


data_file_name = 'gost_8752.html'

# Список идентификаторов таблиц
table_id = 'P0033'

# Состояния буртиков колец в модели (погашен/не погашен)
supressed = 'ПОГАШЕН'
unsupressed = 'НЕ ПОГАШЕН'

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Чтение данных из файла
output_values = []
columns_count = 9
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))
for index in range(15, len(data_values), columns_count):
    d_value = check_value(data_values[index])
    if d_value != '':
        d_backup = d_value
    d_value = d_backup
    D1_value = check_value(data_values[index + 1])
    if D1_value != '':
        D1_backup = D1_value
    D1_value = D1_backup
    D2_value = check_value(data_values[index + 2])
    if D2_value != '':
        D2_backup = D2_value
    D2_value = D2_backup
    h_value = check_value(data_values[index + 5])
    if h_value != '':
        h_backup = h_value
    h_value = h_backup
    h1_value = check_value(data_values[index + 8])
    if h1_value != '':
        h1_backup = h1_value
    h1_value = h1_backup
    for D_value in [D1_value, D2_value]:
        if D_value != '-':
            config_name = '1.1-' + d_value + 'x' + D_value + '-1'
            output_values.append('\t'.join([config_name, d_value, D_value, h_value, h1_value, supressed]))
            config_name = '2.1-' + d_value + 'x' + D_value + '-1'
            output_values.append('\t'.join([config_name, d_value, D_value, h_value, h1_value, unsupressed]))

# Запись данных в файл
with open('ГОСТ 8752 Манжеты.txt', 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values))
