import requests

question = input("User: ")
response = requests.post("http://127.0.0.1:5000/", question)

print("AI: " + response.text)
