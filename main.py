import requests
from twocaptcha import TwoCaptcha
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import secrets
from config import captcaapikey
import string
from os import system

gened = 0
solver = TwoCaptcha(captcaapikey)

system("title " + f"[Bankruptcy]")

def updatetitle():
    system("title " + f"[Bankruptcy] - Total Accounts Generated - {gened}")

def captchaBypass():
    result = solver.hcaptcha(sitekey='77a19f73-4977-46ea-8989-9f73f3b778c5',
                                url='https://create2.cprewritten.net/create_penguin.php')
    print("[Bankruptcy] - Successfully Got Captcha Key")

    return result['code']

def genAcct():
    print("[Bankruptcy] - Getting Captcha Key")
    captchaKey = captchaBypass()
    email = f'{secrets.token_hex(8)}@gmail.com'
    username = secrets.token_hex(5)
    url = "https://create2.cprewritten.net/create_penguin.php"
    Payload = {
        "penguin_name": username,
        'penguin_pass': "penis23sdD@",
        'penguin_email': email,
        'penguin_colour': '1',
        'captcha': captchaKey,
        'subscription': False
    }
    r = requests.post(url, Payload)
    val2 = r.json()['success']
    if val2 == True:
        gened + 1
        updatetitle()
        file = open("Accts.txt", "a")
        file.write(f"{username}:penis23sdD@  \n")
        print(f'[Bankruptcy] - Successfully Generated Account \n[Bankruptcy] - Username: {username} Password: penis23sdD@')
    else:
        print("[Bankruptcy] - There was a error")

if __name__ == '__main__':
    import os
    import threading
    clear = lambda: os.system('cls')
    clear()
    print('''
 _______                       __                                        __                         
/       \                     /  |                                      /  |                        
$$$$$$$  |  ______   _______  $$ |   __   ______   __    __   ______   _$$ |_     _______  __    __ 
$$ |__$$ | /      \ /       \ $$ |  /  | /      \ /  |  /  | /      \ / $$   |   /       |/  |  /  |
$$    $$<  $$$$$$  |$$$$$$$  |$$ |_/$$/ /$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$/   /$$$$$$$/ $$ |  $$ |
$$$$$$$  | /    $$ |$$ |  $$ |$$   $$<  $$ |  $$/ $$ |  $$ |$$ |  $$ |  $$ | __ $$ |      $$ |  $$ |
$$ |__$$ |/$$$$$$$ |$$ |  $$ |$$$$$$  \ $$ |      $$ \__$$ |$$ |__$$ |  $$ |/  |$$ \_____ $$ \__$$ |
$$    $$/ $$    $$ |$$ |  $$ |$$ | $$  |$$ |      $$    $$/ $$    $$/   $$  $$/ $$       |$$    $$ |
$$$$$$$/   $$$$$$$/ $$/   $$/ $$/   $$/ $$/        $$$$$$/  $$$$$$$/     $$$$/   $$$$$$$/  $$$$$$$ |
                                                            $$ |                          /  \__$$ |
                                                            $$ |                          $$    $$/ 
                                                            $$/                            $$$$$$/  
[1] - Generate Accounts
[2] - Check Accounts
[3] - Get Account info
   ''')

    val = input("[Bankruptcy] - Please Enter Which Task You Would Like To Do \n\n")

    if val == "1":
        threadss = input("[Bankruptcy] - Please Enter Threads \n\n")
        threadss = int(threadss)
        def main(threadss):
            thread_list = []
            while True:
                for i in range(threadss):
                    thread = threading.Thread(target=genAcct, args=(), daemon=True)
                    thread.start()
                    thread_list.append(thread)

                for thread in thread_list:
                    thread.join()
        main(threadss)
    elif val == "2":
        print('coming soon')

