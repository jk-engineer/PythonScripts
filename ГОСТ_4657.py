# Данная программа создает список типоразмеров подшипников по ГОСТ 4657.
# http://docs.cntd.ru/document/1200012742
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
    value = value.replace('-', '')
    value = value.replace('/', '_')
    return value


def get_mass(mass_data: list, d: str, table_id: str, name: str):
    """Возвращает значение массы подшипника

    :param mass_data: данные о массе подшипников
    :param d: внутренний диаметр подшипника
    :param table_id: идентификатор таблицы
    :param name: обозначение подшипника
    :return:
    """
    result_value = ''
    # Поиск внутреннего диаметра в списке масс
    start_index = mass_data.index(d)
    # Определение наличия внутреннего кольца подшипника
    if name[:4] == '4244' or name[:4] == '4344' or name[:4] == '4074':
        inner_ring = True
    else:
        inner_ring = False
    # Серия диаметров 8
    if table_id == 'P0026' and inner_ring:
        result_value = mass_data[start_index + 1]
    elif table_id == 'P0026' and not inner_ring:
        result_value = mass_data[start_index + 2]
    # Серия диаметров 9
    if table_id == 'P002A' and inner_ring:
        result_value = mass_data[start_index + 3]
    elif table_id == 'P002A' and not inner_ring:
        result_value = mass_data[start_index + 4]
    # Серия диаметров 1
    if table_id == 'P002D' and inner_ring:
        result_value = mass_data[start_index + 5]
    elif table_id == 'P002D' and not inner_ring:
        result_value = mass_data[start_index + 6]
    return result_value


data_file_name = 'gost_4657.html'

# Список идентификаторов таблиц
tables_id = [
    'P0026',
    'P002A',
    'P002D'
]

# Состояния элементов в модели (погашен/не погашен)
supressed = 'ПОГАШЕН'
unsupressed = 'НЕ ПОГАШЕН'

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)

# Чтение данных из файла
output_values_244000 = []
output_values_254000 = []
output_values_344000 = []
output_values_354000 = []
output_values_74000 = []
output_values_24000 = []
columns_count = 13
mass_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', 'P0059'))
mass_values = [check_value(value) for value in mass_values[15:]]
for id_value in tables_id:
    data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', id_value))
    start_indices = [data_values.index(name) for name in data_values if check_value(name)[:4] == '4244']
    for index in start_indices:
        config_name_244000 = check_value(data_values[index])
        config_name_254000 = check_value(data_values[index + 1])
        config_name_344000 = check_value(data_values[index + 2])
        config_name_354000 = check_value(data_values[index + 3])
        config_name_74000 = check_value(data_values[index + 4])
        config_name_24000 = check_value(data_values[index + 5])
        d_value = check_value(data_values[index + 6])
        D_value = check_value(data_values[index + 7])
        B_value = check_value(data_values[index + 8])
        r_value = check_value(data_values[index + 9])
        Fw_value = check_value(data_values[index + 10])
        mass_value_244000 = get_mass(mass_values, d_value, id_value, config_name_244000)
        mass_value_254000 = get_mass(mass_values, d_value, id_value, config_name_254000)
        mass_value_344000 = get_mass(mass_values, d_value, id_value, config_name_344000)
        mass_value_354000 = get_mass(mass_values, d_value, id_value, config_name_354000)
        mass_value_74000 = get_mass(mass_values, d_value, id_value, config_name_74000)
        mass_value_24000 = get_mass(mass_values, d_value, id_value, config_name_24000)
        output_values_244000.append('\t'.join([config_name_244000, d_value, D_value, B_value, r_value, r_value, Fw_value, mass_value_244000, unsupressed, unsupressed, unsupressed, supressed, supressed]))
        output_values_254000.append('\t'.join([config_name_254000, d_value, D_value, B_value, r_value, r_value, Fw_value, mass_value_254000, supressed, supressed, unsupressed, supressed, supressed]))
        output_values_344000.append('\t'.join([config_name_344000, d_value, D_value, B_value, r_value, r_value, Fw_value, mass_value_344000, unsupressed, unsupressed, unsupressed, unsupressed, supressed]))
        output_values_354000.append('\t'.join([config_name_354000, d_value, D_value, B_value, r_value, r_value, Fw_value, mass_value_354000, supressed, supressed, unsupressed, unsupressed, supressed]))
        output_values_74000.append('\t'.join([config_name_74000, d_value, D_value, B_value, r_value, r_value, Fw_value, mass_value_74000, unsupressed, unsupressed, supressed, supressed, unsupressed]))
        output_values_24000.append('\t'.join([config_name_24000, d_value, D_value, B_value, r_value, r_value, Fw_value, mass_value_24000, supressed, supressed, supressed, supressed, unsupressed]))

# Запись данных в файл
with open('ГОСТ 4657 Подшипники.txt', 'a', encoding='utf-8') as f_out:
    f_out.write('\n'.join(output_values_244000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_254000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_344000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_354000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_74000))
    f_out.write('\n')
    f_out.write('\n'.join(output_values_24000))
