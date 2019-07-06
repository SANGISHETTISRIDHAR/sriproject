
def sendACASMS(contactno = "1234567890", message="sorry"):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS & message="+message+"&language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "cnLsJjdYq3cMNwocVpe3K0VnpEzovV3NVB1p7OP6ghDVushwFXfrOeEvBhQ5",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    d1= response.text
    return d1

