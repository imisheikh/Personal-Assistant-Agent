import requests


user_message = "Can you tell me about cricket sports in 3-4 lines"

request_message = {"message": user_message}

url = "https://imisheikh.app.n8n.cloud/webhook-test/35dc905f-a1e8-4e38-9844-3dae40b8621d"

response = requests.post(url, json=request_message)

print(response.status_code)
print(response.json()[0]["output"])
