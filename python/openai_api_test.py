import os 
import dotenv
import openai 

# set API key
dotenv.load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)

# User Query
Query = input("Enter your query: ")

# create a chat completion
response = openai.ChatCompleation.creatr(
    model : "gpt-4o-mini",
    messages : [
        {"role" : "user", 
         "content" : Query}
    ]

)

print(response)