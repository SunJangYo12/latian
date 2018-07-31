import requests as req

resp = req.get("http://localhost:89/?name=Sunjang")
print "get =========================================="
print resp.text

resp = req.request(method='GET', url="http://localhost:89")
print "request ======================================"
print(resp.text)
print"status========================================="
print(resp.status_code)

resp = req.get("http://localhost:89/ngukuk")
print(resp.status_code)
