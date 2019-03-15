from requests import get, post, delete

cookies = dict(session='eyJjc3JmX3Rva2VuIjoiYzJkYTQ2NGVkZmVkNDU4YzRkMTFkMmE4YmY5ODA0OTgxNDIxMmExYyIsInVzZXJfaWQiOjF9.XItzLw.eGQvt2a6_fRgafoQQF0XExBPZZs')
print(post('http://localhost:8000/api/v1/news',
           json={'title': 'Заголовок', 'content': 'Текст новости', 'user_id': 1}, cookies=cookies).json())
print(get('http://localhost:8000/api/v1/news').json())
print(delete('http://localhost:8000/api/v1/news/5', cookies=cookies).json())
print(get('http://localhost:8000/api/v1/news').json())