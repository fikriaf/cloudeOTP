import time, json, os, sys, random
from requests import get,post
from bs4 import BeautifulSoup as bs
head={
'Host': 'claudeotp.com',
'origin': 'https://claudeotp.com',
'user-agent': 'Mozilla/5.0 (Linux; Android 11; Infinix X662 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36',
'cookie': "csrf_cookie_name=aa8fa57da99844be411e5ca86ac77c95;ci_session=d57f3vf6t0mssunvv4n968huae2q4d6m;remember=126859efe8df734ec0d4508f%3A5e1df0b1ae15ce0b83145a174442063ac6f752d9;tab-panels=promo;agreement=1;information18=1"
}

def getlis():
    getlist=json.loads(get("https://claudeotp.com/api/get-services/d60a9472328d605b781def22ee616261").text)
    for lis in getlist["data"]["data"]:
        print(f"{lis['id']}. {lis['name']}   [Rp {lis['price']}]")
def order(otp):
    if otp == '1':
        dat={
        'aplikasi':'10'
        }
    elif otp == '2':
        dat={
        'aplikasi':'1'
        }
    elif otp == '3':
        dat={
        'aplikasi':'15'
        }
    elif otp == '4':
        dat={
        'aplikasi':'52'
        }

    order=post("https://claudeotp.com/order/create", headers=head, data=dat).text
    if order:
        return order
    else:
        print("gagal order")



if __name__=="__main__":
    print("""
--------------------------------------
            CLAUDEOTP.COM
--------------------------------------""")
    while True:
        getinfo=json.loads(get("https://claudeotp.com/api/get-profile/d60a9472328d605b781def22ee616261").text)
        print(f"""Email       : {getinfo["data"]["data"]["email"]}
Username    : {getinfo["data"]["data"]["username"]}
Saldo       : Rp {getinfo["data"]["data"]["saldo"]}
--------------------------------------
                MENU
--------------------------------------
[1] DANA
[2] GOJEK
[3] OVO
[4] ASTRAPAY
--------------------------------------""")
        mau=input("order [y/n]? ")
        if "y" in mau:
            pilih=input("Pilih nomor : ")
            get_order=order(pilih)

        print("""
--------------------------------------
[1] Refresh
[2] Cancel
--------------------------------------
""")
        while True:
            agree=input("select ? ")
            if agree == "1":
                refresh=get('https://claudeotp.com/order', headers=head).text
                sms=bs(refresh, "html.parser").find_all('div', class_='collapse show')
                #for i in sms:
                print(sms)
                get_sms=bs(sms, "html.parser").find('div', class_='card-body')
                print(get_sms)
            elif agree == "2":
                href=bs(get_order, "html.parser").find_all('a', class_='btn btn-sm btn-danger')
                for i in href:
                    get_href=i['href']
                    print(get_href)
                cancel=get(get_href, headers=head)
                print(cancel)
                break
        #os.system("cls")