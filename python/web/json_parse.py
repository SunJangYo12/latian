import requests as req

data = {'name': 'Jane', 'age': 17}
resp = req.post("http://localhost:89", json=data)
print resp.text
