from main import Acorn

def test_authentication():
    acorn = Acorn()
    response = acorn.authenticateSession()
    assert(response == "Successfully Authenticated")
    acorn.retrieveStudentInfo()



if __name__ == '__main__':
    test_authentication()
