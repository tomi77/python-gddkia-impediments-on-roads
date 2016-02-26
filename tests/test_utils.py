# coding:utf-8
from __future__ import unicode_literals

from datetime import datetime
try:
    from unittest import TestCase, mock
except ImportError:
    from unittest import TestCase
    from mock import mock

from impediments.utils import get_impediments


class TestImpediments(TestCase):
    def setUp(self):
        self.xml = open('tests/fixtures/utrdane.xml')

    @mock.patch('impediments.utils.urlopen')
    def test_x(self, urlopen):
        self.maxDiff = None
        urlopen.return_value = self.xml
        impediments = get_impediments()
        self.assertEqual(len(impediments), 2)
        self.assertListEqual(impediments, [
            {
                'type': 'U',
                'route_number': 'A4',
                'province': 'śląskie',
                'initial_mileage': 333.832,
                'length': 2.220,
                'name': 'Katowice',
                'latitude': 50.255891,
                'longitude': 18.964565,
                'start_date': datetime(2015, 10, 19, 13),
                'end_date': datetime(2016, 2, 24, 10),
                'detour': 'Wymiana i konserwacja ekranów akustycznych wzdłuż '
                          'autostrady A4 na odcinku od km 333+832 do km '
                          '336+052 (od węzła "Bocheńskiego" do Batory , kier '
                          'Wroclaw) . Generalna Dyrekcja Dróg Krajowych i '
                          'Autostrad Oddział w Katowicach informuje o dużym '
                          'prawdopodobieństwie wystąpienia utrudnień w ruchu, '
                          'zarówno w ciągu głównym autostrady, jak i na '
                          'jezdniach zbiorczych. Etap III - Roboty '
                          'zlokalizowane przy jezdni zbiorczej w kierunku '
                          'Wrocławia. Na odcinku jezdni zbiorczej w rejonie '
                          'planowanych robót wprowadzono ograniczenie '
                          'prędkości kolejno do 70 km/h i 50 km/h.',
            },
            {
                'type': 'U',
                'route_number': 'A4',
                'province': 'śląskie',
                'initial_mileage': 346.000,
                'length': 0.800,
                'name': 'Katowice - Kraków',
                'latitude': 50.218676,
                'longitude': 19.120233,
                'start_date': datetime(2016, 2, 19, 20),
                'end_date': datetime(2016, 3, 1),
                'detour': None,
            },
        ])
