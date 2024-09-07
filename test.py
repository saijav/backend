import requests

BASE = "http://127.0.0.1:8000/"

response = requests.get(BASE + "budgets/1")
print(response.json())

input()

response = requests.put(BASE + f"budgets/5", {"id":5, "name":"viides", "amount":0, "spent": 1000, "budget_left": -1000})
print(response.json())

response = requests.put(BASE + "budgets/6", {"id": 6, "name": "kuudes", "amount":5, "spent": 2, "budget_left": 3})
print(response.json())

input()

response = requests.patch(BASE + "budgets/6", {"id": 6, "spent": 1, "budget_left": 2})

input()


response = requests.get(BASE + "budgets/1")
print(response.json())
response = requests.get(BASE + "budgets/2")
print(response.json())
response = requests.get(BASE + "budgets/3")
print(response.json())
response = requests.get(BASE + "budgets/4")
print(response.json())
response = requests.get(BASE + "budgets/5")
print(response.json())
response = requests.get(BASE + "budgets/6")
print(response.json())
response = requests.get(BASE + "budgets/7")
print(response.json())