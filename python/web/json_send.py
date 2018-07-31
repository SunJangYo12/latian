import requests as req

resp = req.get("http://localhost:89")
print resp.json()
