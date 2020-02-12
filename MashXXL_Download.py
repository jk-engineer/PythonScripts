# Программа для скачивания книг с сайта http://mash-xxl.info.
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


import sys
import WebScraper


def get_next_page_url(source_page_url):
    """Возвращает ссылку на следующую страницу.

    :param source_page_url: адрес исходной страницы.
    :return:
    """
    try:
        result_value = list(ws.get_attribute_values_by_element_value(ws.page_parser(source_page_url), 'a', 'href', '[Стр. >>]'))[0]
    except IndexError:
        result_value = ''
    return result_value


ws = WebScraper.WebScraper()
main_url = 'http://mash-xxl.info'
page_url = str(sys.argv[1])
print(page_url)
file_counter = 0
page_number = 0
while True:
    # Ссылка на изображения на текущей странице
    img_url = main_url + list(ws.get_attribute_values(ws.page_parser(page_url), 'img', 'src'))[0]
    # Генерация имени файла, сохранение изображения
    page_number += 1
    file_name = '{num:03d}'.format(num=page_number) + '.png'
    ws.download_file(img_url, file_name)
    file_counter += 1
    # Вывод количества загруженных файлов
    print('Загружено файлов: ' + str(file_counter))
    # Получение прямой ссылки на следующую страницу
    next_page_url = get_next_page_url(page_url)
    page_url = main_url + next_page_url
    if len(next_page_url) != 0:
        # Если прямая ссылка найдена, то цикл начинает обработку новой страницы по полученной ссылке
        continue
    else:
        # Если прямая ссылка не обнаружена, то выполняется переход по ссылке из изображения
        # При этом на странице снова появляется ссылка для перехода на следующую страницу
        temp_url = img_url.replace('pic1', 'page').strip('.png')
        next_page_url = get_next_page_url(temp_url)
        page_url = main_url + next_page_url
        # Если ссылка перехода на следующую страницу не найдена (достигнут конец книги), то выход из цикла
        if len(next_page_url) == 0:
            break
# Отчет об окончании загрузки
print('Загрузка успешно завершена')
