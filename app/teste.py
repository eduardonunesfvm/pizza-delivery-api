import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMiIsImV4cCI6MTc2ODM1ODI5MH0.pffi6s614TXKLqO840tUMXGeIYmt2rz023pjcaHYk20"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers = headers)
print(requisicao)
print(requisicao.json())