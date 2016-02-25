# coding:utf-8
from __future__ import unicode_literals

import time
from datetime import datetime
import xml.dom.minidom as dom

from six.moves.urllib.request import urlopen


XML_URL = 'http://www.gddkia.gov.pl/dane/zima_html/utrdane.xml'


def find_text(node, name):
    return get_text(node.getElementsByTagName(name)[0].childNodes)


def find_int(node, name):
    return get_int(node.getElementsByTagName(name)[0].childNodes)


def find_float(node, name):
    return get_float(node.getElementsByTagName(name)[0].childNodes)


def find_date(node, name):
    return get_date(node.getElementsByTagName(name)[0].childNodes)


def get_text(nodes):
    rc = ""
    for node in nodes:
        if node.nodeType == node.TEXT_NODE:
            rc += node.data
    return rc


def get_int(nodes):
    return int(get_text(nodes))


def get_float(nodes):
    x = get_text(nodes)
    return float(x.replace(',', '.')) if x else 0.0


def get_date(nodes):
    txt = get_text(nodes)[:-6].replace('T', ' ')
    if txt == 'Do odwołania:00':
        return datetime(2099, 12, 31)
    else:
        time_format = '%Y-%m-%d %H:%M:%S'
        st = time.strptime(txt, time_format)
        return datetime(st.tm_year, st.tm_mon, st.tm_mday,
                        st.tm_hour, st.tm_min, st.tm_sec)


def extract(node):
    return {
        'type': find_text(node, 'typ'),
        'route_number': find_text(node, 'nr_drogi'),
        'province': find_text(node, 'woj'),
        'initial_mileage': find_float(node, 'km'),
        'length': find_float(node, 'dl'),
        'name': find_text(node, 'nazwa_odcinka'),
        'latitude': find_float(node, 'geo_lat'),
        'longitude': find_float(node, 'geo_long'),
        'start_date': find_date(node, 'data_powstania'),
        'end_date': find_date(node, 'data_likwidacji'),
        'detour': find_text(node, 'objazd'),
    }


def get_impediments():
    """
    :raise urllib2.URLError | urllib.error.URLError: When
    :return:
    """
    fh = urlopen(XML_URL)

    doc = dom.parse(fh)
    xml = doc.documentElement

    nodes = xml.getElementsByTagName('utr')
    impediments = [extract(node) for node in nodes]

    return impediments
