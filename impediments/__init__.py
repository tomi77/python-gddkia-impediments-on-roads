from __future__ import absolute_import

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import xml.dom.minidom as dom

from .models import Impediment

VERSION = (0, 1, 0, 'beta', 1)
__author__ = 'Tomasz Jakub Rup'
__email__ = 'tomasz.rup@gmail.com'
__version__ = '0.1b1'
__license__ = 'MIT'

XML_URL = 'http://www.gddkia.gov.pl/dane/zima_html/utrdane.xml'


def get_impediments():
    """
    :raise urllib2.URLError | urllib.error.URLError: When
    :return:
    """
    fh = urlopen(XML_URL)

    doc = dom.parse(fh)
    xml = doc.documentElement

    nodes = xml.getElementsByTagName('utr')
    impediments = [Impediment(node) for node in nodes]

    return impediments
