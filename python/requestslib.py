import requests 

# status function
def status(websitename,response):

    if response == 200:
        return (f"{websitename} found")
    elif response == 404:
        return (f"{websitename} not found")
    elif response == 503:  
        return (f"{websitename} service unavailable")
    elif response == 999:
        return (f"{websitename} request denied")
    else:
        return (f"{websitename} have other issue {response} ")

# parameters 
params = { 
    'name': 'aleen',
    'age': '43'
}

# data to be sent to the server
payload = { 
    'name': 'aleen',
    'age': '43'
}

# Make a GET request to the URLs
response = requests.get('https://www.linkedin.com/in/lama-almushyqih')
print(status("linkedin",response.status_code))

response = requests.get('https://www.google.com')
print(status("google",response.status_code))


# specific web service HTTPbin.org
response = requests.post('http://HTTPbin.org/post', data=payload)
print(status("HTTPbin",response.status_code))

res_json = response.json()
del res_json['origin']
print("content " + str(res_json))

