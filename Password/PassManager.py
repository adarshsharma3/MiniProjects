from cryptography.fernet import Fernet


class PassManager:

    def __init__(self):
        self.key=None
        self.passwordFile=None
        self.passwordDict={}


    def createKey(self,path):
        self.key=Fernet.generate_key()
        with open(path,'wb') as f:
            f.write(self.key)  

    def load_key(self,path):
        with open(path,'rb') as f:
            self.key=f.read() 
    
    def createFile(self,path,initial_value=None):
        self.passwordFile=path

        if initial_value is not None:
            for key,value in initial_value.items():
                self.add_password(key,value) 


    def load_password_file(self,path):
        self.passwordFile=path

        with open(path, 'r') as f:
         for line in f:
            site , encrytpted =line.split(":")
            self.passwordDict[site]=Fernet(self.key).decrypt(encrytpted.encode()).decode()

    def add_password(self,site,password):
        self.passwordDict[site]=password

        if self.passwordFile is not None:
            with open(self.passwordFile,'a+') as f:
                encrytpted=Fernet(self.key).encrypt(password.encode())
                f.write(site+":"+encrytpted.decode()+"\n")


    def get_password(self, site ):
        return self.passwordDict[site]



def main():
    password={
        "utube":"123",
        "face":"sdf"
    }        
pm =PassManager()

print("""Select One?
(1) create a key
(2) load an existing key
(3) Create a password file
(4) Load existing password file
(5) Add new Pass
(6) Get your pass
(q) Quit
"""
)


check=false

while not chck:

    choice= input("Enter the option number")
    if choice =="1":
        path =input("Enter the path: ")
        pm.createKey(path)
    elif choice =="2":
        path =input("Enter the path: ")
        pm.load_key(path)   
    elif choice =="3":
        path =input("Enter the path: ")
        pm.createFile(path ,password)
    elif choice =="4":
        path =input("Enter the path: ")
        pm.load_password_file(path)              
    elif choice =="5":
        site =input("Enter sit : ")
        paswrd=input("Enter the password")
        pm.add_password(site,paswrd)   
    elif choice =="6":
        site =input("which site")
        print(f"Heres your password : {pm.get_password(site)}")

    elif choice=="q":
        check=True
        print("Bhaag ja yaha se")
    else:
        print("invalid Choice")

if __name__=="__main__":
    main()                          
