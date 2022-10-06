class Password_manager():
    
    def __init__(self,name):
        self.name = name
        self.old_password = []

    def old_passwords(self):
        return self.old_password 

    def get_password(self):
        return self.old_password[-1] if len(self.old_password)!=0 else "Please, set password firstly"

    def set_password(self,password):
        self.old_password.append(password)

    def is_correct(self,check):
        return True if check==self.old_password[-1] else False

user = Password_manager("ICE")

print(user.old_passwords())

user.set_password("ICE2003")
print(user.get_password())

user.set_password("ICE2003")
user.set_password("ICE_2003")
print(user.get_password())
print(user.old_passwords())

print(user.is_correct("ICE2003"))
print(user.is_correct("ICE_2003"))