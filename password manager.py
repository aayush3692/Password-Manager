from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()        
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
        
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        return key
    
def view(fer):
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            value = line.rstrip()
            name, password = value.split("|")
            print("Name: "+name+ "| Password: "
                +fer.decrypt(password.encode()).decode())               
            
def add(fer):
    with open("passwords.txt", "a") as file:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        
        file.write(name + "|"+ fer.encrypt(password.encode()).decode() + "\n")           
    
def main():    
    while True: 
            key = load_key() 
            fer = Fernet(key)
            print("Enter the operation to perform: ")
            print("1. View")
            print("2. Add")
            print("3. Quit")
            
            choice = input("Enter your choice(1-3): ")
            
            if choice == '1':
                view(fer)
            elif choice == '2':
                add(fer)  
            elif choice == '3':
                break 

if __name__ == "__main__":
    main()