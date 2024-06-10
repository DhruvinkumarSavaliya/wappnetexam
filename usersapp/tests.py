from django.test import TestCase

# Create your tests here.
from rest_framework.test import RequestsClient

client = RequestsClient()
response = client.post('http://localhost:8000/api/login/', json={
    'username': 'test',
    'password': 'test'
})
assert response.status_code == 200

response = client.post('http://localhost:8000/api/register/', json={
    'username': 'test',
    'password': 'test'
})
assert response.status_code == 400


response = client.post('http://localhost:8000/api/register/', json={
    'username': 'test5',
    'password': 'test5'
})
assert response.status_code == 200

response = client.post('http://localhost:8000/api/books/', json={
    'name': 'book tailes',
    'author': '1', 
    'publisher': '1'
})
assert response.status_code == 200


response = client.get('http://localhost:8000/api/books/1', json={
})
assert response.status_code == 200
