# Данная программа создает список типоразмеров гвоздей по ГОСТ 4028.
# http://docs.cntd.ru/document/1200004058
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
    value = value.replace('х', 'x')
    return value


data_file_name = 'gost_4028.html'

# Список идентификаторов таблиц
table_id_1 = 'P0023'
table_id_2 = 'P0041'

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Чтение данных из файла
output_values = []
columns_count = 2
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id_1))
for index in range(2, len(data_values), columns_count):
    d_value = check_value(data_values[index])
    if d_value != '':
        d_backup = d_value
    d_value = d_backup
    l_value = check_value(data_values[index + 1])
    D_value = str(float(d_value.replace(',', '.')) * 2).replace('.', ',')
    h_value = str(float(d_value.replace(',', '.')) * 0.6).replace('.', ',')
    config_name = 'П ' + d_value + 'x' + l_value
    output_values.append('\t'.join([config_name, d_value, l_value, D_value, h_value]))

columns_count = 4
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id_2))
for index in range(4, len(data_values), columns_count):
    d_value = check_value(data_values[index])
    if d_value != '':
        d_backup = d_value
    d_value = d_backup
    l_value = check_value(data_values[index + 1])
    D_value = check_value(data_values[index + 3])
    if D_value != '':
        D_backup = D_value
    D_value = D_backup
    h_value = str(float(d_value.replace(',', '.')) * 0.6).replace('.', ',')
    config_name = 'К ' + d_value + 'x' + l_value
    output_values.append('\t'.join([config_name, d_value, l_value, D_value, h_value]))

# Запись данных в файл
with open('ГОСТ 4028 Гвозди.txt', 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values))
