import random
from random import choice
import requests
import json

# # r = requests.post(authtoken+' http://localhost:8000/api/', json={"title": "wedwdrf", "text": "wedrfqwedrs"})
# # print(r.json())
# token = "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRlc2l0eSIsImV4cCI6MTUxODM2MTUyOCwiZW1haWwiOiJkZXNkZXNAdWtyLm5ldCJ9.tHL_0831dWgQQElN5SHJ2pHNbOiay0X4656lwpHsRxc"
# url = 'http://localhost:8000/api/'
# data = {'title': 'wedwdrf', 'text': 'wedrfqwedrs'}
# headers = {'Authorization': token, 'Content-Type': 'application/json'}
# k = requests.post(url, json=data, headers=headers).json()
# print(k)
#

# ------------------add likes/dislikes------------------
# r = requests.get('http://127.0.0.1:8000/api/').json()
# x = []
# for post in r:
#     x.append(post['id'])
#
# add_like_dislike = []
# i = 1
# while i < 50:
#     add_like_dislike += (random.sample(x, 1))
#     i += 1
# print(add_like_dislike)
# print(random.choice([True, False]))
# addlikedislike = requests.post(
#             'http://127.0.0.1:8000/api/post/203/addlike/',
#             json={'value': 'true'},
#             headers={'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRlc2l0eSIsImV4cCI6MTUxODM4NTE4MiwiZW1haWwiOiJkZXNkZXNAdWtyLm5ldCJ9.1xtwBJlcsFrj3-BO4ZCAnVs9RbNftQUYruuWa-9pyDI',
#                      'Content-Type': 'application/json'}).json()
file = open('bot.txt', 'r')
print(file.read().split('\n')[0].split(' = ')[1])