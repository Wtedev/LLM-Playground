import requests

proxies = {
  'http': '139.99.237.62:80',

}
response = requests.get ('http://HTTPbin.org/get', proxies=proxies)
res_json = response.json()
print("content " + str(res_json))