import unittest
from unittest.mock import *
import Zadanie2
class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.temp = Zadanie2.Subscriber()

    def test_add_new_client(self):
        clients = [{'id': 1, 'client': 'client1'}]
        self.temp.addClient = MagicMock(return_value=clients)
        self.assertEqual(self.temp.addClient(1, 'client1'), clients)
    def test_add_new_id_bool(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, False, 'x')

    def test_add_new_client(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, 1, [])

    def test_add_new_dict(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, 1, {})

    def test_add_new_id(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, '1', 'x')

    def test_add_new_cients(self):
        clients = [{'id': 1, 'client': 'client1'}, {'id': 2, 'client': 'client2'}, {'id': 3, 'client': 'client3'}]
        self.temp.addClient = MagicMock(return_value=clients)
        self.assertEqual(self.temp.addClient(3, 'client3'), clients)


    def test_del_client(self):
        clients = [{'id': 1, 'client': 'client1'}, {'id': 2, 'client': 'client2'}]
        self.temp.delClient = MagicMock(return_value=clients)
        self.assertEqual(self.temp.delClient(3), clients)


    def test_del_array(self):
        self.temp.delClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.delClient, [])

    def test_del_tuple(self):
        self.temp.delClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.delClient, ())

    def test_del_float(self):
        self.temp.delClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.delClient, 1.2)
    def test_no_client_delete(self):
        self.temp.delClient = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.delClient, 5)

    def test_del_string(self):
        self.temp.delClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.delClient, '5')

    def test_message(self):
        self.temp.sendMsg = MagicMock(return_value='Hello')
        self.assertEqual(self.temp.sendMsg(1, 'Hello'), 'Hello')

    def test_msg_id_string(self):
        self.temp.sendMsg = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.sendMsg, '1', 'hello')

    def test_msg_id_tuple(self):
        self.temp.sendMsg = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.sendMsg, (), 'hello')

    def test_msg_msg_int(self):
        self.temp.sendMsg = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.sendMsg, 1, 1)

    def test_msg_msg_bool(self):
        self.temp.sendMsg = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.sendMsg, 1, True)