import requests as req

resp = req.head("http://localhost:89")

print("Server: " + resp.headers['server'])
print("Last modified: " + resp.headers['last-modified'])
print("Content type: " + resp.headers['content-type'])
print("Content length: " + resp.headers['content-length'])
