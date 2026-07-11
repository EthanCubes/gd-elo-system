import requests

url = "https://www.boomlings.com/database/getGJUserInfo20.php"

data = {
    "secret": "Wmfd2893gb7",
    "targetAccountId": "31268368"
}
headers = {
    "User-agent": "",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=data, headers=headers)
print(response.text)