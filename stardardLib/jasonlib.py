import json
import pandas as pd 

url = 'https://raw.githubusercontent.com/despresj/portfolio/main/misc/karabiner.json'
resp = requests.get(url)
data = json.loads(resp.text)

print(data)

print(json.dumps(data, indent=2))
data.keys()

data['global'].keys()
out = []
for item in data["profiles"]:
    print(item)
    
[x for x in out]

print(json.dumps(data, indent=2))
print(json.dumps(data["profiles"], indent=2))

prof = data["profiles"]
[x for x in prof]

df = pd.json_normalize(data)



currency_url = "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"



resp = requests.get(currency_url)
data = json.loads(resp.text)



