# Модуль с функциями парсинга html-страниц.
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


# Для корректной работы требуется:
#   Python версии 3.x
#   Установленные пакеты BeautifulSoup4, requests

import requests
import shutil
import typing
from bs4 import BeautifulSoup as bSoup


class WebScraper():
    """Класс для парсинга html-страниц.
    """
    def __init__(self):
        self.__session_object = requests.Session()


    @property
    def session_object(self):
        """Возвращает объект сессии.

        :return:
        """
        return self.__session_object


    def page_parser(self, source_url: str) -> 'BeautifulSoup':
        """Возвращает страницу, обработанную html-парсером.

        :param source_url: страница, обработанная html-парсером.
        :return:
        """
        result = self.__session_object.get(str(source_url))
        page = result.text
        return bSoup(page, 'html.parser')


    def page_parser_from_file(self, file_name: str) -> 'BeautifulSoup':
        """Возвращает страницу, обработанную html-парсером

        :param file_name: имя файла.
        :return:
        """
        return bSoup(open(str(file_name), encoding='utf-8'), 'html.parser')


    def get_attribute_values(self, parsed_page: 'BeautifulSoup', tag: str, element_attribute: str) -> typing.Generator[str, None, None]:
        """Возвращает список значений атрибутов заданных элементов.

        :param parsed_page: страница, обработанная html-парсером.
        :param tag: тег элемента.
        :param element_attribute: атрибут, значение которого будет включено в список.
        :return:
        """
        return (str(element.get(str(element_attribute))) for element in parsed_page.find_all(str(tag)))


    def get_attribute_values_by_attribute_value(self, parsed_page: 'BeautifulSoup', tag: str, element_attribute: str, mask_element_attribute: str,
                                                mask_element_attribute_substring: str) -> typing.Generator[str, None, None]:
        """Возвращает список значений атрибутов элементов при условии, что значение атрибута-маски содержит искомый текст.

        :param parsed_page: страница, обработанная html-парсером.
        :param tag: тег элемента.
        :param element_attribute: атрибут, который будет добавлен в список.
        :param mask_element_attribute: атрибут-маска, по которому производится поиск ссылок.
        :param mask_element_attribute_substring: искомый текст в значении атрибута-маски
        :return:
        """
        for element in parsed_page.find_all(str(tag)):
            if str(element.get(str(mask_element_attribute))).lower().count(str(mask_element_attribute_substring).lower()) > 0:
                yield str(element.get(str(element_attribute)))


    def get_attribute_values_by_element_value(self, parsed_page: 'BeautifulSoup', tag: str, element_attribute: str, element_value_substring: str) -> typing.Generator[str, None, None]:
        """Возвращает список значений атрибутов элементов при условии, что значение элемента содержит искомый текст.

        :param parsed_page: страница, обработанная html-парсером.
        :param tag: тег элемента.
        :param element_attribute: атрибут, который будет добавлен в список.
        :param element_value_substring: искомый текст в значении элемента.
        :return:
        """
        for element in parsed_page.find_all(str(tag)):
            if str(element.text).lower().count(str(element_value_substring).lower()) > 0:
                yield str(element.get(str(element_attribute)))


    def get_element_values(self, parsed_page: 'BeautifulSoup', tag: str, element_attribute: str, attribute_values: list) -> typing.Generator[str, None, None]:
        """Возвращает список значений элементов.

        :param parsed_page: страница, обработанная html-парсером.
        :param tag: тег элемента.
        :param element_attribute: атрибут элемента.
        :param attribute_values: список-маска значений атрибутов элементов. Если атрибут входит в данный список,
                                то значение элемента добавляется в итоговый список.
        :return:
        """
        for element in parsed_page.find_all(str(tag)):
            if str(element.get(str(element_attribute))) in list(attribute_values):
                yield str(element.text)


    def get_element_values_by_attribute_value(self, parsed_page: 'BeautifulSoup', tag: str, element_attribute: str, attribute_value_substring: str) -> typing.Generator[str, None, None]:
        """Возвращает список значений элементов при условии, что в значении атрибута элемента содержится искомый текст.

        :param parsed_page: страница, обработанная html-парсером.
        :param tag: тег элемента.
        :param element_attribute: атрибут элемента.
        :param attribute_value_substring: искомый текст в значении атрибута.
        :return:
        """
        for element in parsed_page.find_all(str(tag)):
            if str(element.get(str(element_attribute))).lower().count(str(attribute_value_substring).lower()) > 0:
                yield str(element.text)


    def download_file(self, file_url, file_name):
        """Скачивает файл по указанной ссылке.

        :param file_url: ссылка на файл.
        :param file_name: имя, с которым будет сохранен файл.
        """
        result = self.__session_object.get(str(file_url), stream = True)
        with open(str(file_name), 'wb') as f_out:
            result.raw.decode_content = True
            shutil.copyfileobj(result.raw, f_out)
