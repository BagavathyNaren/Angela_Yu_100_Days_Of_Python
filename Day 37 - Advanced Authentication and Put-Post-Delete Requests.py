import requests
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hjkh34h3jk4hj34h3jh6",
    "username": "nanbag007",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, verify=False, json=user_params)
# print(response.text)


"""
{"message":"Success. Let's visit https://pixe.la/@nanbag007 , it is your profile page!","isSuccess":true}

{"message":"This user already exist.","isSuccess":false}

"""

USERNAME = "nanbag007"
TOKEN = "hjkh34h3jk4hj34h3jh6"
GRAPH_ID = "graph1"


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Habit",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=graph_endpoint, verify=False, json=graph_config, headers=headers)
#print(response.text)


"""
{"message":"Success.","isSuccess":true}


{"message":"This graph already exist.","isSuccess":false}

https://pixe.la/v1/users/nanbag007/graphs/graph1.html

"""
graph_configuration = {
    "id": GRAPH_ID,
    "name": "Coding Habit",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many python sections did you complete on Udemy: 100 day of Python => Angela Yu today? ")
}

response = requests.post(url=pixel_creation_endpoint, verify=False, json=pixel_data, headers=headers)
print(response.text)

"""
{"message":"Success.","isSuccess":true}


How to format the Python date to any format we need?

The strftime() method is used for formatting dates in Python.

Example:
```python
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
```

"""


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "1"
}

# response=requests.put(url=update_endpoint, verify=False, json=new_pixel_data, headers=headers)
# print(response.text)


"""
{"message":"Success.","isSuccess":true}

"""

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response=requests.delete(url=delete_endpoint, verify=False, headers=headers)
print(response.text)

"""
{"message":"Success.","isSuccess":true}

"""


