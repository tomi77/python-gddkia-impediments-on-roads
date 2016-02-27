# coding:utf-8
from __future__ import unicode_literals

import time
from datetime import datetime
import xml.dom.minidom as dom

from six.moves.urllib.request import urlopen  # pylint: disable=import-error


XML_URL = 'http://www.gddkia.gov.pl/dane/zima_html/utrdane.xml'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_node_val(node, name):
    try:
        node = node.getElementsByTagName(name)[0].childNodes[0]
        return node.data if node.nodeType == node.TEXT_NODE else None
    except IndexError:
        return None


def get_text(node, name):
    return get_node_val(node, name)


def get_int(node, name):
    val = get_node_val(node, name)
    return int(val) if val else None


def get_float(node, name):
    val = get_node_val(node, name)
    return float(val) if val else None


def get_date(node, name):
    val = get_node_val(node, name)[:-5].replace('T', ' ')
    if val == 'Do odwołania:00':
        return None
    else:
        val = time.strptime(val, TIME_FORMAT)
        return datetime(val.tm_year, val.tm_mon, val.tm_mday,
                        val.tm_hour, val.tm_min, val.tm_sec)


def extract(node):
    return {
        'type': get_text(node, 'typ'),
        'route_number': get_text(node, 'nr_drogi'),
        'province': get_text(node, 'woj'),
        'initial_mileage': get_float(node, 'km'),
        'length': get_float(node, 'dl'),
        'name': get_text(node, 'nazwa_odcinka'),
        'latitude': get_float(node, 'geo_lat'),
        'longitude': get_float(node, 'geo_long'),
        'start_date': get_date(node, 'data_powstania'),
        'end_date': get_date(node, 'data_likwidacji'),
        'detour': get_text(node, 'objazd'),
    }


def get_impediments():
    """
    :raise urllib2.URLError | urllib.error.URLError: When
    :return:
    """
    file = urlopen(XML_URL)

    doc = dom.parse(file)
    xml = doc.documentElement

    nodes = xml.getElementsByTagName('utr')
    impediments = [extract(node) for node in nodes]

    return impediments
