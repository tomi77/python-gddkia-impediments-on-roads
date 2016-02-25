# coding:utf-8
from __future__ import unicode_literals

import time
from datetime import datetime


class XMLModel(object):
    def find_text(self, node, name):
        return self.get_text(node.getElementsByTagName(name)[0].childNodes)

    def find_int(self, node, name):
        return self.get_int(node.getElementsByTagName(name)[0].childNodes)

    def find_float(self, node, name):
        return self.get_float(node.getElementsByTagName(name)[0].childNodes)

    def find_date(self, node, name):
        return self.get_date(node.getElementsByTagName(name)[0].childNodes)

    @staticmethod
    def get_text(nodes):
        rc = ""
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                rc += node.data
        return rc

    def get_int(self, nodes):
        return int(self.get_text(nodes))

    def get_float(self, nodes):
        x = self.get_text(nodes)
        return float(x.replace(',', '.')) if x else 0.0

    def get_date(self, nodes):
        txt = self.get_text(nodes)[:-6].replace('T', ' ')
        if txt == 'Do odwołania:00':
            return datetime(2099, 12, 31)
        else:
            time_format = '%Y-%m-%d %H:%M:%S'
            st = time.strptime(txt, time_format)
            return datetime(st.tm_year, st.tm_mon, st.tm_mday,
                            st.tm_hour, st.tm_min, st.tm_sec)


class Impediment(XMLModel):
    def __init__(self, node):
        self.type = self.find_text(node, 'typ')
        self.route_number = self.find_text(node, 'nr_drogi')
        self.province = self.find_text(node, 'woj')
        self.initial_mileage = self.find_float(node, 'km')
        self.length = self.find_float(node, 'dl')
        self.name = self.find_text(node, 'nazwa_odcinka')
        self.latitude = self.find_float(node, 'geo_lat')
        self.longitude = self.find_float(node, 'geo_long')
        self.start_date = self.find_date(node, 'data_powstania')
        self.end_date = self.find_date(node, 'data_likwidacji')
        self.detour = self.find_text(node, 'objazd')
