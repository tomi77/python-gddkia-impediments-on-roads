# coding:utf-8
from __future__ import unicode_literals

from datetime import datetime
try:
    from unittest import TestCase, mock
except ImportError:
    from unittest import TestCase
    from mock import mock

from impediments.utils import get_impediments


class TestUtils(TestCase):
    @mock.patch('impediments.utils.urlopen')
    def test_get_impediments(self, urlopen):
        file = open('tests/fixtures/utrdane.xml')
        urlopen.return_value = file

        impediments = get_impediments()

        self.assertEqual(len(impediments), 3)
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
            {
                'type': 'U',
                'route_number': '1',
                'province': 'łódzkie',
                'initial_mileage': 381.099,
                'length': 1.234,
                'name': 'Głuchów - Tuszyn',
                'latitude': 51.557778,
                'longitude': 19.594314,
                'start_date': datetime(2015, 6, 29, 7),
                'end_date': None,
                'detour': 'Budowa węzła Tuszyn w ciągu budowanej dr A-1. '
                          'Utrudnienia dotycza skrzyżowania dr nr 1 od km '
                          '382+333-385+027 i dr nr 91c od km 0+000-1+045',
            }
        ])
