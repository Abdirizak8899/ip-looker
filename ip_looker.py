import requests
import json
ip_addr = input('Enter ip address : ').strip()
# 192.145.168.88
def pop_data(data):
    for key  in data:
        print(key ," : ",data.get(key))

def IP_ddress():
    api_url = 'https://api.api-ninjas.com/v1/iplookup?address={}'.format(ip_addr)
    response = requests.get(api_url, headers={'X-Api-Key': 'illML6cZ3q677VHSpCeUnA==QAv56pdQLABaZiUs'})
    if response.status_code == requests.codes.ok:
        resp = response.text
        res = json.loads(resp)
        pop_data(res)
    else:
        print("Error:", response.status_code, response.text)
IP_ddress()

