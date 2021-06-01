# Программа скачивает документы НП "ОПЖТ" с официального сайта (раздел "Стандарты и своды правил"):
# http://opzt.ru/category/tehnicheskoe-regulirovanie/standarty-i-svody-pravil/
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


# Для корректной работы требуется:
#   Python версии 3.x
#   Установленные пакеты BeautifulSoup4, requests


import os
import WebScraper
import HyperLinksCreator as Hlc


main_url = 'http://opzt.ru'
start_url = main_url + '/category/tehnicheskoe-regulirovanie/standarty-i-svody-pravil/'
# Ссылки на все страницы с документами
ws = WebScraper.WebScraper()
pages_links = list(ws.get_attribute_values_by_attribute_value(ws.page_parser(start_url), 'a', 'href', 'class', 'pages-link'))
document_links = []
document_names = []
file_names = []
parsed_page = ''
for page_url in pages_links:
    parsed_page = ws.page_parser(page_url)
    # Ссылки на документы
    document_links.extend([link for link in ws.get_attribute_values(parsed_page, 'a', 'href')
                           if str(link).count('document') > 0])
    # Имена документов
    document_names.extend(list(ws.get_element_values(parsed_page, 'a', 'href', document_links)))
# Имена файлов (применено ограничение длины имени)
filename = ''
file_extension = ''
for doc_num in range(0, len(document_names)):
    filename = str(document_names[doc_num]).replace('/', '')
    if len(filename) > 100:
        filename = filename[:90]
    file_extension = os.path.splitext(document_links[doc_num])[1]
    file_names.append(filename + '_{num:02d}'.format(num=doc_num + 1) + file_extension)
# Скачивание документов
download_doc_counter = 0
download_url = ''
for doc_num in range(0, len(document_links)):
    if str(document_links[doc_num]).count(main_url) == 0:
        download_url = main_url + document_links[doc_num]
    else:
        download_url = document_links[doc_num]
    ws.download_file(download_url, file_names[doc_num])
    download_doc_counter += 1
    print('Загружено файлов: ' + str(download_doc_counter))
# Создание файла в формате .html, в котором содержатся полные названия документов
Hlc.create_hyperlinks_from_names('!Список стандартов и сводов правил ОПЖТ.html', file_names, document_names)
print('Загрузка файлов завершена')
