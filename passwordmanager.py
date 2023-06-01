from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key) '''



def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key


key = load_key() 
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #gets rid of \n when viewing
            user, passw = data.split("|")
            decrypted_pwd = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_pwd)
                
def add():
    name = input("Account Name: ")
    pwd =  input("Password: ")

    with open('passwords.txt', 'a') as f:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view exisitng ones? (view, add)? Type Q to quit  ")
    if mode == "Q":
        break
   
    if mode == "view": 
        view()
    elif mode == "add":
        add()
    else:
        print ("Invalid mode.")
        continue