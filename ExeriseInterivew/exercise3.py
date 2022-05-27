#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Yongli"

"""
Exercise for interview 
/Material/Instructions_for_Python_exercises
"""
import pytz
from datetime import datetime, timedelta


def output_not_ok_response(log_file):
    """
    print non-successful response 4xx,5xx
    :param log_file: file path
    :return:
    """

    with open(log_file, "r", encoding="utf-8") as log:
        next(log)
        for line in log:
            l_line = line.split(",")
            if l_line[3].startswith(("4", "5")):
                not_ok_response_format(l_line)


def not_ok_response_format(l_line):
    """
    format error message
    :param l_line: 4xx,5xx message detail
    :return:
    """
    if not isinstance(l_line, list) or len(l_line)== 0:
        return None
    timestamp = l_line[0]
    label = l_line[2]
    response_code = l_line[3]
    response_msg = l_line[4]
    failure_msg = l_line[8]

    date = datetime(1970, 1, 1) + timedelta(seconds=int(timestamp[0:10]))
    datetime_pst = date.astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S PT')
    print("""
            Time:{}\n
            ResponseCode:{}\n
            ResponseMsg:{}\n
            FailureMsg:{}\n
            Label:{}
            """.format(datetime_pst,response_code,response_msg,failure_msg,label))


if __name__ == '__main__':
    output_not_ok_response("Materials/Jmeter_log1.jtl")
    output_not_ok_response("Materials/Jmeter_log2.jtl")






