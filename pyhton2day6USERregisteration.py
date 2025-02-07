class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

    def display_info(self):
        print(f"Name: {self.name} \nemail: {self.email} \nPassword: {'*' * len(self.password)}")

user_database=[]

def is_email_unique(email):
    for user in user_database:
        if user.email == email:
             return False
    return True

    
def validate_email(email):
     return '@' in email and '.' in email.split('@')[-1]


def user_registration():
    name=input("Enter the name: ")

    while True:
        email=input("Enter the email: ")

        if not validate_email(email):
            print("invalid email. Enter a valid email")
            continue

        if not is_email_unique(email):
            print("email already in use. Enter a different email.")
            continue
        break
    
            
    password=input("Enter the password: ")
    
    new_user=User(name,email,password)
    user_database.append(new_user)
    print("User registered successfully")


user_registration()
