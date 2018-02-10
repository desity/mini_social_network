import random

import requests

number_of_users = 1
max_posts_per_user = 1
max_likes_per_user = 1
try:
    file = open('bot.txt', 'r')
    settings = file.read()
    number_of_users = int(settings.split('\n')[0].split(' = ')[1])
    max_posts_per_user = int(settings.split('\n')[1].split(' = ')[1])
    max_likes_per_user = int(settings.split('\n')[2].split(' = ')[1])
    print(settings)
except:
    print('Something wrong with settings file. Bot is working with default values')
# -----------register users----------------
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
passlen = 8
i = 1
registered_users = {}
while i <= number_of_users:
    user = "".join(random.sample(s, passlen))
    email = "user" + i.__str__() + "@ukr.net"
    r = requests.post('http://127.0.0.1:8000/api/register/', json={"email": email,
                                                                   "username": user,
                                                                   "password": "Desity12"})
    print(user+'  register status code: '+r.status_code.__str__())
    if r.status_code == 201:
        rt = requests.post('http://127.0.0.1:8000/api-token-auth/', json={"username": user,
                                                                          "password": "Desity12"})
        get = rt.json()
        token = get['token']
        registered_users.update({user: {'username': user, 'token': token}})
    i += 1

# -----------add posts by users----------------
print('------------------add posts------------------------')
for user in registered_users:
    i = 0
    print('------------------add post by ' + registered_users[user]['username'] + '------------------------')
    while i < max_posts_per_user:
        i += 1
        addpost = requests.post(
            'http://localhost:8000/api/',
            json={'title': 'Title nomber ' + i.__str__() + ' of ' + registered_users[user]['username'],
                  'text': 'Text ' + i.__str__() + ' of ' + registered_users[user]['username']},
            headers={'Authorization': 'JWT ' + registered_users[user]['token'],
                     'Content-Type': 'application/json'}).json()

        print(addpost)

# ------------------add likes/dislikes------------------
print('------------------add like/dislike------------------------')
posts = requests.get('http://127.0.0.1:8000/api/').json()
post_ids = []
for post in posts:
    post_ids.append(post['id'])
for user in registered_users:
    i = 1
    print('------------------add like/dislike ' + registered_users[user]['username'] + '------------------------')
    while i < max_likes_per_user:
        addlikedislike = requests.post(
            'http://127.0.0.1:8000/api/post/' + random.sample(post_ids, 1)[0].__str__() + '/addlike/',
            json={"value": random.choice([True, False])},
            headers={'Authorization': 'JWT ' + registered_users[user]['token'],
                     'Content-Type': 'application/json'}).json()
        print(addlikedislike)
        i += 1