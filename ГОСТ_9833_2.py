# Данная программа создает список типоразмеров канавок для уплотнительных колец по ГОСТ 9833.
# http://docs.cntd.ru/document/1200017923
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


# Для корректной работы требуется:
#   Python версии 3.x
#   Установленные пакеты BeautifulSoup4, requests


import WebScraper


def check_value(value: str) -> str:
    """Возвращает none, если значение является прочерком

    :param value: проверяемое значение
    :return:
    """
    value = str(value).replace('-', 'none')
    value = value.replace('\n', '')
    return value


data_file_name = 'ГОСТ 9833-73.html'
# Список идентификаторов таблиц радиальных уплотнений
radial_tables_id = [
    'P00C5',
    'P00CF',
    'P00D9',
    'P00E3',
    'P00ED',
    'P00F6',
    'P00FF',
    'P0108'
]
# Список идентификаторов таблиц торцевых уплотнений
flat_tables_id = [
    'P0112',
    'P011C',
    'P0125',
    'P012E',
    'P0138',
    'P0141',
    'P014A',
    'P0153',
    'P015C'
]
b_flat_values = [
    '1,0',
    '1,4',
    '1,85',
    '2,2',
    '2,6',
    '3,3',
    '4,2',
    '5,5',
    '6,5'
]

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Получение общих списков с данными
radial_values = []
for id_value in radial_tables_id:
    radial_values += list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
flat_values = []
temp_values_1 = []
temp_values_2 = []
for id_value in flat_tables_id:
    temp_values_1 = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
    for index in range(0, len(temp_values_1)):
        if str(temp_values_1[index]).count('-') > 0 and len(temp_values_1[index]) > 6:
            temp_values_2.append(temp_values_1[index])
            temp_values_2.append(temp_values_1[index + 1])
            temp_values_2.append(temp_values_1[index + 2])
            temp_values_2.append(b_flat_values[flat_tables_id.index(id_value)])
flat_values += temp_values_2

# Формирование списка значений для радиальных уплотнений
output_radial_values = ['\t'.join(['Название_конфигурации', 'd', 'D', 'd3', 'D1', 'b'])]
radial_value = ''
ring_name = ''
d_radial = ''
D_radial = ''
d3_radial_slide = ''
D1_radial_slide = ''
b_radial_slide = ''
d3_radial_fixed = ''
D1_radial_fixed = ''
b_radial_fixed = ''
for index in range(0, len(radial_values)):
    radial_value = str(radial_values[index])
    if radial_value.count('-') > 0 and len(radial_value) > 6:
        ring_name = radial_value + '_подв.'
        d_radial = radial_values[index + 1]
        D_radial = radial_values[index + 2]
        d3_radial_slide = check_value(radial_values[index + 3])
        D1_radial_slide = check_value(radial_values[index + 4])
        if len(radial_values[index + 5]) > 0:
            b_radial_slide = check_value(radial_values[index + 5])
        if d3_radial_slide != 'none' and len(d3_radial_slide) != 0 and D1_radial_slide != 'none' and len(D1_radial_slide) != 0:
            output_radial_values.append('\t'.join([ring_name, d_radial, D_radial, d3_radial_slide, D1_radial_slide, b_radial_slide]))
        ring_name = radial_value + '_неподв.'
        d3_radial_fixed = check_value(radial_values[index + 6])
        D1_radial_fixed = check_value(radial_values[index + 7])
        if len(radial_values[index + 8]) > 0:
            b_radial_fixed = check_value(radial_values[index + 8])
        if d3_radial_fixed != 'none' and len(d3_radial_fixed) != 0 and D1_radial_fixed != 'none' and len(D1_radial_fixed) != 0:
            output_radial_values.append('\t'.join([ring_name, d_radial, D_radial, d3_radial_fixed, D1_radial_fixed, b_radial_fixed]))

# Формирование списка значений для торцовых уплотнений
output_flat_values = ['\t'.join(['Название_конфигурации', 'd4', 'D2', 'b'])]
flat_value = ''
ring_name = ''
d4_flat = ''
D2_flat = ''
b_flat = ''
for index in range(0, len(flat_values)):
    flat_value = flat_values[index]
    if flat_value.count('-') > 0 and len(flat_value) > 6:
        ring_name = flat_value
        d4_flat = flat_values[index + 1]
        D2_flat = flat_values[index + 2]
        b_flat = flat_values[index + 3]
        output_flat_values.append('\t'.join([ring_name, d4_flat, D2_flat, b_flat]))

# Запись данных в файлы
with open('ГОСТ 9833 Радиальные канавки.txt', 'w', encoding='utf-8') as fout1:
    fout1.write('\n'.join(output_radial_values))

with open('ГОСТ 9833 Торцовые канавки.txt', 'w', encoding='utf-8') as fout2:
    fout2.write('\n'.join(output_flat_values))
