
class jsonKlasa(object):
    def __init__(self):
        import requests, json
        url = requests.get('https://randomuser.me/api/')
        self.jsonObjekt = json.loads(url.text)
#klasa=jsonKlasa()
#print(klasa.getJson()['results'])

