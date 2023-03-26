import requests, json
def send_sms(username,mobile_number):
    # url = "https://www.fast2sms.com/dev/bulkV2"
    # payload = "sender_id=FSTSMS&message=Hello%20"+username+"%20your%20request%20has%20been%20submitted%20successfully.&language=english&route=p&numbers="+mobile_number+"&flash=1"
    # headers = {'Authorization': 'Pdq0LSzO8IV7img6aHGrvnpwEZjYl59NXxW4fsytD32RQhbFuBopqCQJyYn3mdw4vj6BUF29sT7taxEh',
    #            'Content-Type': 'application/x-www-form-urlencoded',
    #            'Cache-Control': 'no-cache',}
    # response = requests.request("POST", url, data=payload, headers=headers)
    # print(response.text)



    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"Pdq0LSzO8IV7img6aHGrvnpwEZjYl59NXxW4fsytD32RQhbFuBopqCQJyYn3mdw4vj6BUF29sT7taxEh",
    "sender_id":"FSTSMS",
    "message":"hello",
    "language":"english",
    "route":"q",
    "flash" : 1,
    "numbers": mobile_number}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)