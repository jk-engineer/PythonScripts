# Данная программа создает список типоразмеров уплотнительных колец по ГОСТ 9833.
# http://docs.cntd.ru/document/1200017923
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


data_file_name = 'ГОСТ 9833-73.mht'
# Список идентификаторов таблиц с кольцами
ring_tables_id = [
    'P003A',
    'P0042',
    'P004B',
    'P0054',
    'P005D',
    'P0066',
    'P006E',
    'P0077',
    'P0080'
]

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)
# Чтение данных из файла
output_values = []
for id_value in ring_tables_id:
    data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
    for index in range(0, len(data_values)):
        value = str(data_values[index])
        value = value.replace(' ', '')
        value = value.replace('\n', '')
        if value.count('-') > 0 and len(value) > 6:
            d1 = str(data_values[index + 2])
            d2 = value[-2] + ',' + value[-1]
            output_values.append('\t'.join([value + '-2-2', d1, d2]))

# Запись данных в файлы
with open('ГОСТ 9833 Кольца.txt', 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values))
