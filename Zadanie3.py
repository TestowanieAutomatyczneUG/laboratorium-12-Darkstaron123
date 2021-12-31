import unittest
from unittest.mock import *
class MailServer(object):
    def __init__(self):
        pass
    def sendMessage(self,templateEngine):
        pass
class TemplateEngine(object):
    def __init__(self):
        pass
    def useTemplate(self,recipent,sender,message):
        pass
class Messenger(object):
    def __init__(self):
        self.TemplateEngine=TemplateEngine()
        self.MailServer=MailServer()
    def sendMessageThroughghMailServer(self,recipent,sender,message):
        self.MailServer.sendMessage(self.TemplateEngine.useTemplate(recipent,sender,message))
    def receiveMessagesFromMailServer(self):
        return self.MailServer.getNewMessages()
#Messenger().sendMessageThroughghMailServer("bob","bobOdbiorca","Bobie odbierz pls")
