import requests

r = requests.get("https://www.tureng.com")
print(r.status_code)
print(r.ok)