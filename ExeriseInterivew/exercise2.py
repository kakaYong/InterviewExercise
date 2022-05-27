#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Yongli"

"""
Exercise for interview 
/Material/Instructions_for_Python_exercises
"""

import json
import copy

__test_payload = "Materials/test_payload.json"


def remove_element_itself(element):
    """
    remove element from given json and create a new updated json file
    :param json element: ele
    :return str: new modified json file
    """
    with open(__test_payload, 'r') as ori_f:
        org_data = json.load(ori_f)
    # avoid runtime error "try to change dictionary during iteration"
    copy_org_data = copy.copy(org_data)
    find_element_and_del(org_data, copy_org_data, element)
    print(org_data)
    # Create new file
    with open("OutPut/new_test_payload.json", 'w') as new_f:
        json.dump(org_data, new_f)


def find_element_and_del(dict_items, copy_di, element):

    """
    recursion for all nested dictionary
    :return:
    """
    for x, y in copy_di.items():
        if x == element:
            del dict_items[x]
        elif isinstance(y, dict):
            # avoid runtime error "try to change dictionary during iteration"
            copy_y = copy.copy(y)
            find_element_and_del(y, copy_y, element)


if __name__ == '__main__':
    remove_element_itself("outParams")
    remove_element_itself("appdate")








