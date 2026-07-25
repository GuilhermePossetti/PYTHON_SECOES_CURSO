# request para requisições HTTP

import requests 

# quando o um site começa com http:// quer dizer que está rodando na porta 80
# quando o um site começa com https:// quer dizer que está rodando na porta 443
url = 'http://localhost:3333/'
response = requests.get(url)

# print(response.status_code)
# print(response.headers)
# print(response.content) #bytes
print(response.text)
# print(response.json())