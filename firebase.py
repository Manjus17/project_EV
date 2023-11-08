import pyrebase
from ui_start import Ui_StartWindow

firebaseConfig = {
    "apiKey": "AIzaSyCxe5iXVQujXMltkX7Lcc06Xp16qRCzi1Y",
    "authDomain": "ev-station-management-e64ee.firebaseapp.com",
    "databaseURL": "https://ev-station-management-e64ee-default-rtdb.firebaseio.com/",
    "projectId": "ev-station-management-e64ee",
    "storageBucket": "ev-station-management-e64ee.appspot.com",
    "messagingSenderId": "361415870891",
    "appId": "1:361415870891:web:173208fcd67f36eea46aee",
    "measurementId": "G-9HD0M30NVD",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

#Login function

def login():
    print("Log in...")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        # print(auth.get_account_info(login['idToken']))
       # email = auth.get_account_info(login['idToken'])['users'][0]['email']
       # print(email)
    except:
        print("Invalid email or password")
    return

#Signup Function

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask=input("Do you want to login?[y/n]")
        if ask=='y':
            login()
    except: 
        print("Email already exists")
    return

#Main

ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()


