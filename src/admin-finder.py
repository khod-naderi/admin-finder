import requests
import sys
import validators
from random import randint
from re import sub

def RandomStr(length):
    """
    get random strings 
    (length) is len string output
    """
    output = ""
    for i in range(0,length): output += chr(randint(65,122)) # A = 65, z=122
    return output

def Get_404_Original(rootUrl):
    """
    Get page 404 to bypass (<?php http_response_code(404); ?> and ...)
    """
    while(True):
        # (start)
        url = rootUrl + "/" + RandomStr(8) # url 404 page 
        request = requests.get(url) # send request
        if request.status_code != 404: continue # If this page is not 404 then goto (start) 
        return sub(url,"",request.text)  # If this page is 404 then return content By deleting the url 404

def check_url(url): 
    check = validators.url(url)
    if check == True:
        return(True)    
    else:
        return(False)

def path_list():
    fresh_list = list()
    file_path = open("path_login.txt", "r")
    for line in file_path: fresh_list.append(line)
    file_path.close()
    return fresh_list  

def check_content(content):
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

def about():
    banner = """
    ++++++++++++++++++++++++++++++++++++
    
    #   Coded By PentestoR

    #   version -----> 0.1

    #   Contact -----> t.me/nulllbyte 
    
    #   Channel -----> t.me/PrivateProgramming  

    ++++++++++++++++++++++++++++++++++++
    
    """
    print(banner)

def help():
    banner = """
    ========================================
    
    Usage :
    python admin-finder.py https://target.com

    ========================================
    """
    print(banner)

if __name__ == "__main__":
    checked_list = []
    try:
        var = sys.argv[1]
        if "-h" in var or "--help" in var:
            help()
        elif check_url(var) == True:
            list_path = path_list()
            for l in list_path:
                while(True):
                    try:
                        # Merge root site to path
                        url = var + "/" + l 
                        url = url.strip()
                        try:
                            r = requests.get(url=url)
                            status_code = r.status_code
                            print(f"[*] {url} : {status_code}")
                            #print(Get_404_Original(var) + ("-"*30) + "\n" + r.text)
                            if (status_code == 200 or status_code == 302 or status_code == 403 or status_code == 401) and (check_content(str(r.content)) == True):
                                checked_list.append(url)
                            elif (status_code == 404 and (Get_404_Original(var) != sub(url,"",r.text))):
                                checked_list.append(url)
                            break
                        except requests.exceptions.ConnectionError:
                            print("[!] ERROR IN CONNECTION URL....")
                    except:
                        continue
            count = len(checked_list)
            print(f"[~~] {count} Results Detected")
            n = 0
            if count > 0:
                for t in checked_list:
                    n+=1
                    print(f"{n} ---> {t}")                
        elif check_url(var) == False:
            print("[#] Invalid Url! Please check Url.")

    except IndexError:
        about()
        help()        