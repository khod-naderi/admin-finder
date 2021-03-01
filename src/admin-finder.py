import requests
import sys
from re import sub
from admin_finder import admin_finder


if __name__ == "__main__":
    checked_list = [] # output list
    Afinder = admin_finder() 
    try:
        var = sys.argv[1] 
        if "-h" in var or "--help" in var: 
            # Show Help Page
            admin_finder.help()
        elif Afinder.check_url(var):
            # if URL is valid
            for path in Afinder.path_list(): # get path 
                while(True):
                    try:
                        # Merge root site to path
                        url = var + "/" + path.strip()
                        url = url.strip()
                        try:
                            r = requests.get(url=url)
                            status_code = r.status_code
                            print(f"[*] {url} : {status_code}")
                            if (status_code == 200 or status_code == 302 or status_code == 403 or status_code == 401) and (Afinder.check_content(str(r.content)) == True):
                                # finded normal page
                                checked_list.append(url)
                            elif (status_code == 404 and (Afinder.Get_404_Original(var) != sub(url,"",r.text))):
                                # finded hiden page
                                checked_list.append(url)
                            break
                        except requests.exceptions.ConnectionError:
                            print("[!] ERROR IN CONNECTION URL....")
                    except KeyboardInterrupt:
                        # Press CTRL+C
                        admin_finder.show(checked_list)
                    except:
                        continue
            # end 
            admin_finder.show(checked_list)         
        else:
            # URL dont valid
            print("[#] Invalid Url! Please check Url.")
    except IndexError:
        admin_finder.about()
        admin_finder.help()        