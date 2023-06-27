import sys, os 


class User:
    def __init__(self , username , email , password , is_admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin
        
        
    def add_user(self , username , email , password , is_admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin
    
    def get_user_info(self):
        return self.username , self.email , self.password , self.is_admin

        
    
    