import requests as req
import re

resp = req.get("http://localhost:89")
content = resp.text
stript = re.sub('<[^<]+?>','', content)
print stript
