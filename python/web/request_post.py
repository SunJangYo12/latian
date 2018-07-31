import requests as req

d = {'name': 'Sunjang'}
resp = req.post("http://localhost:89", d)
print resp.text
