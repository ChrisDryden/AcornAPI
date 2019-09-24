import requests
from bs4 import BeautifulSoup


ACORN_HOST = "https://acorn.utoronto.ca"
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
}


class Acorn:
    def __init__(self):
        self.session = requests.Session()

    def authenticateSession(self, username, password):
        response = self.session.get(urlTable['authURL2'], headers=formHeader)
        initial_login = BeautifulSoup(response.text)
        hidden_tags = initial_login.find_all("input", type="hidden")
        request_body = {} 
        for tag in hidden_tags:
            request_body[tag['name']] = tag['value']
        request_body['user'] = username
        request_body['pass'] = password
        login_request = self.session.post(url=urlTable['authURL2'], headers=formHeader, data=request_body)
        print(login_request.text)
        return "Successfully Authenticated"
    def enrollCourse(self, courseID):
        enrolledCart = "https://acorn.utoronto.ca/sws/rest/enrolment/term-course-loads" 
        studentParams = {
            "primaryOrgCode": "ASPC",
            "postCode": "AECPEBASC",
            "sessionCodes": 20199,
            "sessionCodes": 20201,
        }
        response = session.get(enrolledCart, headers=headers, params=studentParams)
    def retrieveStudentInfo(self):
        studentInfoUrl = "https://acorn.utoronto.ca/sws/rest/profile/studentRegistrationInfo"
        studentInfo = self.session.get(studentInfoUrl, headers=formHeader)
        print(studentInfo.text)


#https://acorn.utoronto.ca/sws/rest/enrolment/term-course-loads?primaryOrgCode=APSC&postCode=AECPEBASC&sessionCodes=20199&sessionCodes=20201


#testing = session.get(url="https://www.acorn.utoronto.ca", headers=formHeader)
#print(testing.text)
