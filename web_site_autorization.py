import requests
from bs4 import BeautifulSoup

class Interpals(object):
    url='http://www.interpals.net/'

    def auth(self):
        session=requests.Session()
        url = self.url+'/login.php'
        params={
        'action':u'login',
        'auto_login':1,
        'login': u'*******',
        'password':u'*******'
        }
        r=session.post(url, params)

        print(r.text)




if __name__ == '__main__':
    interpals= Interpals()
    interpals.auth()
