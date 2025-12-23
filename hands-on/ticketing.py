import requests 
url="https://ticketing.com/create"

payload={
    "event": "Concert",
    "date": "2024-09-15",
    "tickets": 2,
}

headers={Content-Type: application/json}

response=requests.post(url,json=payload,headers=headers)
if response.status_code==201:
    print("Ticket created successfully")
else:
    print("Failed to create ticket")
    