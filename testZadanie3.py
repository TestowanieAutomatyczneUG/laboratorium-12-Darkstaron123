import Zadanie3
from unittest import TestCase
from unittest.mock import *
class TestMessenger(TestCase):
    def setUp(self):
        self.temp = Zadanie3.Messenger()

    @patch.object(Zadanie3.Messenger, "sendMessageThroughghMailServer")
    def test_send_mock_sendMessageThroughghMailServer(self, mock_sendMessageThroughghMailServer):
        mock_sendMessageThroughghMailServer.return_value = 'Message has been sent'
        self.assertEqual(self.temp.sendMessageThroughghMailServer('bob@example.com','bob2@example.com', 'message'), 'Message has been sent')

    @patch.object(Zadanie3.Messenger, "receiveMessagesFromMailServer")
    def test_receiveMessagesFromMailServer(self, mock_receiveMessagesFromMailServer):
        mock_receiveMessagesFromMailServer.return_value = ['1', '2']
        self.assertEqual(self.temp.receiveMessagesFromMailServer('bob@example.com'), ['1', '2'])