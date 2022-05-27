#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Yongli"

"""
Exercise for interview 
/Material/Instructions_for_Python_exercises
"""

from datetime import date, timedelta
import sys

__test_payload1 = "Materials/test_payload1.xml"  # TODO move to configure.ini


def update_departure_return(x_days_ahead, y_days_ahead):
    """
    Create a new xml file base on new date
    :param int x_days_ahead:
    :param int y_days_ahead:
    :return: date
    """

    if not isinstance(x_days_ahead, int) and not isinstance(y_days_ahead, int):
        return None

    new_departure_date = date.today() + timedelta(days=x_days_ahead)

    new_return_date = date.today() + timedelta(days=y_days_ahead)

    new_file_xml(__test_payload1, str(new_departure_date).replace("-", ""), str(new_return_date).replace("-", ""))

    return new_departure_date, new_return_date


def new_file_xml(file_physical_path, new_departure_date,new_return_date):
    """
    update xml element and create a new file
    :param file_physical_path:
    :param new_departure_date:
    :param new_return_date:
    :return:
    """
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    try:
        tree = ET.parse(file_physical_path)
        root = tree.getroot()
    except Exception as e:
        print("Error: Cannot parse file:%s" % file_physical_path)
        sys.exit(1)

    _depart = root.findall(path=".//DEPART")
    _return = root.findall(path=".//RETURN")
    if len(_depart) != 0 and len(_return) != 0:
        _depart[0].text = new_departure_date
        _return[0].text = new_return_date
    else:
        return None

    tree.write("OutPut/new_test_payload1.xml", xml_declaration=True)


if __name__ == '__main__':
    print(update_departure_return(100, 2000))

