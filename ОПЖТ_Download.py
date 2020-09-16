# Программа скачивает документы НП "ОПЖТ" с официального сайта:
# http://www.opzt.ru/node/469
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
import HyperLinksCreator as Hlc


starter = input('Начать выполнение загрузки? Y/N')
if starter.lower() == 'y':
    ws = WebScraper.WebScraper()
    main_url = 'http://www.opzt.ru'
    documents_url = main_url + '/node/469'
    download_doc_counter = 0
    all_document_names = []
    all_file_names = []
    while True:
        # Ссылка на следующую страницу
        try:
            next_page_link = list(ws.get_attribute_values_by_element_value(ws.page_parser(documents_url), 'a', 'href', 'следующая'))[0]
        except IndexError:
            next_page_link = ''
        # Ссылки на документы
        document_links = [link for link in ws.get_attribute_values(ws.page_parser(documents_url), 'a', 'href') if str(link).count('pdf') > 0]
        # Имена документов
        document_names = list(ws.get_element_values(ws.page_parser(documents_url), 'a', 'href', document_links))
        # Имена файлов (применено ограничение длины имени файла не более 100 символов)
        file_names = [name[:90].replace('"', '') + '....pdf' for name in document_names]
        # Общие списки имен файлов и документов для последующего создания сводного файла
        all_document_names.extend(document_names)
        all_file_names.extend(file_names)
        # Скачивание документов
        for doc_num in range(0, len(document_links)):
            ws.download_file(document_links[doc_num], file_names[doc_num])
            download_doc_counter += 1
            print('Загружено файлов: ' + str(download_doc_counter))
        documents_url = main_url + next_page_link
        if len(next_page_link) == 0:
            break
    print('Загрузка файлов завершена')
    # Создание файла в формате .htm, в котором содержатся полные названия документов
    Hlc.create_hyperlinks_from_names('!Список документов ОПЖТ.htm', all_file_names[::-1], all_document_names[::-1])
    print('Итоговый файл создан')
    input('Нажмите Enter для выхода')
else:
    print('Загрузка отменена')
    input('Нажмите Enter для выхода')
