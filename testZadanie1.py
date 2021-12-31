import unittest
import Zadanie1
class Zadanie1bezUzyciaAtrap(unittest.TestCase):
    def setUp(self):
        self.jsonKlasa=Zadanie1.jsonKlasa()
    def test_json_object_is_existing(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt),dict)
    def test_results_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results']), list)
    def test_results_gender_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results'][0]['gender']), str)
    def test_results_name_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results'][0]['name']), dict)
    def test_results_name_title_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results'][0]['name']['title']), str)
    def test_results_name_first_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results'][0]['name']['first']), str)
    def test_results_name_last_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results'][0]['name']['last']), str)
    def test_results_location_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results'][0]['location']), dict)
    def test_results_location_street_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results'][0]['location']['street']), dict)
    def test_results_location_city_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results'][0]['location']['city']), str)
    def test_results_location_state_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['results'][0]['location']['state']), str)
    # i tak dalej
    def test_info_attribute_good_type(self):
        self.assertEqual(type(self.jsonKlasa.jsonObjekt['info']),dict)

from unittest.mock import Mock
class Zadanie1zUzyciemAtrapy(unittest.TestCase):

    def setUp(self):
        import json
        with open('atrapa.json') as json_file:
            self.jsonObjekt=Mock()
            self.jsonObjekt=json.load(json_file)
    def test_json_object_is_existing(self):
        self.assertEqual(type(self.jsonObjekt),dict)
    def test_results_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results']), list)
    def test_results_gender_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results'][0]['gender']), str)
    def test_results_name_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results'][0]['name']), dict)
    def test_results_name_title_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results'][0]['name']['title']), str)
    def test_results_name_first_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results'][0]['name']['first']), str)
    def test_results_name_last_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results'][0]['name']['last']), str)
    def test_results_location_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results'][0]['location']), dict)
    def test_results_location_street_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results'][0]['location']['street']), str)
    def test_results_location_city_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results'][0]['location']['city']), str)
    def test_results_location_state_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['results'][0]['location']['state']), str)
    # i tak dalej
    def test_info_attribute_good_type(self):
        self.assertEqual(type(self.jsonObjekt['info']),dict)
