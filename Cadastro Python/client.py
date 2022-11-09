import requests

#data = {"username":"jadson", "secret":"@admin456", "info":"salario", "value":6000}
#data = {"username":"jadson", "secret":"@admin456", "nome":"matheus", "cargo":"Engenheiro", "salario":"7000"}

#response = requests.post("http://0.0.0.0:5000/register", data= data)

response = requests.get("http://0.0.0.0:5000/empregados")

if response.status_code == 200:
    message = response.json()
    print(message['empregados'])
else:
    print(response.status_code)