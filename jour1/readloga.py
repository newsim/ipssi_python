#!/usr/bin/python3

from datetime import datetime

import os

apath = os.path.expanduser("~/a.log")
print("chemin etendu en", apath)
with open(apath) as fd:
    for line in fd:
        # print(line)
        # print(line.split())
        # print(line.split(None, 11))
        ip, login, passws, date, zone, reqtype, \
        url, httptype, status, size, referer, \
        uagenttrash = line.split(None, 11)
        print(ip)
        # print(date)
        # print(date[1:])
        # exemple de stack overflow
        # datetime_object = datetime.strptime('Jun 1 2005  1:33PM',
        #                                     '%b %d %Y %I:%M%p')
        # datetime_object = datetime.strptime('29/Oct/2019:06:25:25',
        #                                     '%d/%b/%Y:%H:%M:%S')
        datetime_object = datetime.strptime(date[1:],
                                            '%d/%b/%Y:%H:%M:%S')
        print(datetime_object)
        print(uagenttrash)
        break
