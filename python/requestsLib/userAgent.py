import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'image/webp'
}
response = requests.get('http://HTTPbin.org/image', headers=headers)
print ( "Response Code: " + str(response.status_code) )

with open('Data/scriptingimage.webp', 'wb') as image:
    image.write(response.content )