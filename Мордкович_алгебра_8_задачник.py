# Программа для скачивания задачника "ГДЗ по алгебре 8 класс Мордкович, Александрова, Мишустина Мнемозина".
# https://www.euroki.org/gdz/ru/algebra/8_klass/reshebnik-po-algebre-8-klass-mordkovich-aleksandrova-fgos-775/zadachi-na-povtorenie-zadanie-1
# Copyright (C) 2021 Evgeniy Ipatov

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
#   Python версии 3.6 или выше
#   Установленные пакеты BeautifulSoup4, requests


from bs4 import BeautifulSoup as bSoup
import certifi
from WebScraper import WebScraper


ws = WebScraper()
base_url = 'https://www.euroki.org'
target_url = 'https://www.euroki.org/gdz/ru/algebra/8_klass/reshebnik-po-algebre-8-klass-mordkovich-aleksandrova-fgos-775/zadachi-na-povtorenie-zadanie-1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
ws.session_object.verify = certifi.where()
ws.session_object.headers = headers
while True:
    parsed_page = bSoup(ws.session_object.get(target_url).text, 'html.parser')
    image_element = [element for element in parsed_page.find_all('img', class_='gdz_image')][0]
    image_url = image_element.get('src')
    image_title = image_element.get('title')
    file_name = f'{image_title.replace("ГДЗ по алгебре 8 класс Мордкович, Александрова, Мишустина Мнемозина ответы и решения онлайн ", "")}.png'
    file_name = file_name.replace(':', '')
    ws.download_file(image_url, file_name)
    print(file_name)
    next_page_url_list = [element.get('href') for element in parsed_page.find_all('a', class_='btn btn-default') if element.text == 'Следующий »']
    if len(next_page_url_list) == 0:
        break
    else:
        target_url = base_url + next_page_url_list[0]
print('Done!')
