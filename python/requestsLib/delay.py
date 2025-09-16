import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
}


response= requests.get('http://Httpbin.org/delay/3', headers=headers,)
print(response.status_code)

res_json = response.json()
del res_json['origin']
print("content " + str(res_json))

