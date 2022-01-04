import requests
from twocaptcha import TwoCaptcha
import secrets
from config import captcaapikey

solver = TwoCaptcha(captcaapikey)

def captchaBypass():
    result = solver.hcaptcha(sitekey='77a19f73-4977-46ea-8989-9f73f3b778c5',
                                url='https://create2.cprewritten.net/create_penguin.php')
    print("Successfully Got Captcha Key")

    return result['code']

def genAcct():
    print("Getting Captcha Key")
    captchaKey = captchaBypass()
    username = secrets.token_hex(8)
    email = f'{secrets.token_hex(8)}@gmail.com'
    url = "https://create2.cprewritten.net/create_penguin.php"
    Payload = {
        "penguin_name": secrets.token_hex(8),
        'penguin_pass': "penis23sdD@",
        'penguin_email': email,
        'penguin_colour': '1',
        'captcha': captchaKey,
        'subscription': False
    }
    r = requests.post(url, Payload)
    if r.status_code == 200:
        file = open("Accts.txt", "w")
        file.write(f"{email}:penis23sdD@\n")
        print(f'successfully Generated Account \n Email: {email} Password: penis23sdD@')
genAcct()
