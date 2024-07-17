import requests

BASE = "http://127.0.0.1:8000/"

response = requests.patch(BASE + "budget/2", {"spent": 900, "budget_left": 100})

#response = requests.put(BASE + "budget/3", {"id":3, "name":"toka", "amount":10000, "spent": 1000, "budget_left": 9000})
#print(response.json())

#response = requests.put(BASE + "budget/4", {"id": 4, "name": "eka", "amount":2700, "spent": 1000, "budget_left": 1700})
#print(response.json())

#input()

#response = requests.delete(BASE + "budget/2")
#print(response)

#input()

response = requests.get(BASE + "budget/2")
print(response.json())