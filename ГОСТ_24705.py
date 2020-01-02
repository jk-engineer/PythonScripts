# Данная программа создает список шагов диаметров метрических резьб по ГОСТ 24705.
# http://docs.cntd.ru/document/1200038934/
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


# Для корректной работы требуется:
#   Python версии 3.x
#   Установленные пакеты BeautifulSoup4, requests


import WebScraper
import CheckNumber as chNum


data_file_name = 'ГОСТ 24705-2004.html'
# Идентификатор таблицы с данными по резьбам
table_id = 'P003E'
columns_count = 5

ws = WebScraper.WebScraper()
page = ws.page_parser_from_file(data_file_name)
data_values = list(ws.get_element_values_by_attribute_value(page, 'p', 'id', table_id))

# Список диаметров начинается со значения 0,25 мм, поэтому необходимо найти индекс соответствующего элемента
start_index = data_values.index('0,25')
# Номинальный/наружный диаметр резьбы
d_nom = ''
# Шаг резьбы
pitch_value = ''
# Средний диаметр резьбы
d_mid = ''
# Внутренний диаметр резьбы
d_min = ''
# Внутренний диаметр резьбы по дну впадины
d_min1 = ''
# Обозначение резьбы
thread_title = ''
# Номинальный/наружный диаметр резьбы (для восстановления пустых значений)
d_nom_backup = ''

output_values = []

for index in range(start_index, len(data_values), columns_count):
    d_nom, pitch_value, d_mid, d_min, d_min1 = data_values[index:index + columns_count]
    d_nom = str(d_nom).replace(' ', '')
    # В обозначении резьбы крупный шаг не указывается. Мелкий шаг должен быть указан
    if d_nom == '':
        # Считывание предыдущего значения диаметра
        d_nom = d_nom_backup
        thread_title = 'M' + d_nom + 'x' + pitch_value
    else:
        d_nom_backup = d_nom
        thread_title = 'M' + d_nom
    output_values.append('\t'.join([thread_title, d_nom, pitch_value, d_mid, d_min, d_min1]))

# Запись данных в файл
with open('ГОСТ 24705 Резьбы метрические.txt', 'w', encoding='utf-8') as fout:
    fout.write('\n'.join(output_values))
