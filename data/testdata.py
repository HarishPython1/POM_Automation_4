import os

# URL="http://localhost/login.do"
#URL = "https://phptravels.com/"

URL="https://www.flipkart.com/"
USERNAME = "admin"
PASSWORD = "manager"

MAX_WAIT = 60
MED_WAIT = 30
MIN_WAIT = 15


def generic_path():
    path = os.getcwd().replace("\\data", "")
    print(path)


generic_path()
