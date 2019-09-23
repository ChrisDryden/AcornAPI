import requests
from bs4 import BeautifulSoup

session = requests.Session()

ACORN_HOST = "https://acorn.utoronto.ca";
urlTable = {
    "authURL1": ACORN_HOST + "/sws",
    "authURL2": "https://weblogin.utoronto.ca/",
    "authURL3": "https://idp.utorauth.utoronto.ca/PubCookie.reply",
    "acornURL": ACORN_HOST + "/spACS"
}

formHeader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.110 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html'
};


def authenticateSession(username, password):
    response = session.get(urlTable['authURL2'], headers=formHeader)
    initial_login = BeautifulSoup(response.text)
    hidden_tags = initial_login.find_all("input", type="hidden")
    request_body = {} 
    for tag in hidden_tags:
        request_body[tag['name']] = tag['value']
    request_body['user'] = username
    request_body['pass'] = password
    login_request = session.post(url=urlTable['authURL2'], headers=formHeader, data=request_body)



#Test this program with
#authenticateSession(username, password):

testing = session.get(url="https://www.acorn.utoronto.ca", headers=formHeader)
print(testing.text)
