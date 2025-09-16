import requests 

# Make a GET request to the URLs
response = requests.get('https://www.linkedin.com/in/lama-almushyqih')
print("Your status code is for LinkedIn account " + str(response.status_code))

response = requests.get('https://www.google.com')
print("Your status code is for Google " + str(response.status_code))

