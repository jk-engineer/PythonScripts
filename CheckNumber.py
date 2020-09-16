# Модуль с функциями проверки численных значений
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


def is_number(value: str) -> bool:
    """Возвращает True, если значение является числом.

    :param value: проверяемое значение.
    :return:
    """
    value = str(value).replace(',', '.')
    try:
        float(value)
        return True
    except(TypeError, ValueError):
        return False
