import validators
from random import randint
from re import sub
import requests

class admin_finder():
    def __init__(self):
        pass

    @staticmethod
    def show(checked_list):
        """
        show Results output and end 
        """
        count = len(checked_list) # get content len
        print(f"[~~] {count} Results Detected")
        n = 0
        if count > 0:
            for t in checked_list:
                n+=1
                print(f"{n} ---> {t}")
        exit()     
    
    def path_list(self):
        """
        Get Path at File (path_login.txt) and yield
        """
        # fresh_list = list()
        file_path = open("path_login.txt", "r")
        # for line in file_path: fresh_list.append(line)
        for line in file_path:
            yield line
        file_path.close()
        return ""

    def RandomStr(self,length):
        """
        get random strings 
        (length) is len string output
        """
        output = ""
        for i in range(0,length): output += chr(randint(65,122)) # A = 65, z=122
        return output

    def Get_404_Original(self,rootUrl):
        """
        Get page 404 to bypass (<?php http_response_code(404); ?> and ...)
        """
        while(True):
            # (start)
            url = rootUrl + "/" + self.RandomStr(8) # url 404 page 
            request = requests.get(url) # send request
            if request.status_code != 404: continue # If this page is not 404 then goto (start) 
            return sub(url,"",request.text)  # If this page is 404 then return content By deleting the url 404

    def check_url(self,url): 
        """
        Check URL in Valid
        """
        check = validators.url(url)
        if check == True:
            return(True)    
        else:
            return(False)

    

    def check_content(self,content):
        """
        Check if Content have [check_list]
        """
        check_list = [
            "username",
            "password",
            "Username",
            "Password",  
            "email",
            "mail",
            "number",
            "ID",
            "user",
            "pass",
            
        ]
        for c in check_list:
            if c.upper() in content or c.lower() in content or c in content:
                return(True) 
    
    @staticmethod
    def about():
        """
        About Page
        """
        banner = """
        ++++++++++++++++++++++++++++++++++++
        
        #   Coded By PentestoR

        #   version -----> 0.1

        #   Contact -----> t.me/nulllbyte 
        
        #   Channel -----> t.me/PrivateProgramming  

        ++++++++++++++++++++++++++++++++++++
        
        """
        print(banner)

    @staticmethod
    def help():
        """
        Help Page
        """
        banner = """
        ========================================
        
        Usage :
        python admin-finder.py https://target.com

        ========================================
        """
        print(banner)
