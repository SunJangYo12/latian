import requests as req
import re

resp = req.get("http://localhost:89")
print"semua========================================"
print(resp.text)

content = resp.text

stripped = re.sub('<[^<]+?>', '', content)
print"isi web======================================"
print(stripped)
