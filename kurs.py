import requests

import info

resp = requests.get('https://api.vk.com/method/users.get',
params = {
    'access_token': info.service_key,
    'user_ids': '217033641',
    'fields': 'bdate, sex',
    'name_case': 'nom',
    'v': info.version
})
all_members_list = [resp.json()['response'][0]]
resp = requests.get('https://api.vk.com/method/friends.get',
params = {
    'access_token': info.service_key,
    'user_id': '217033641',
    'count': 5,
    'fields': 'bdate, sex',
    'name_case': 'nom',
    'v': info.version
})

member_list = resp.json()['response']['items']


for member in member_list:
    member['friend_of'] = '217033641'
    all_members_list.append(member)
    resp = requests.get('https://api.vk.com/method/friends.get',
                        params={
                            'access_token': info.service_key,
                            'user_id': member['id'],
                            'count': 5,
                            'fields': 'bdate, city, sex',
                            'name_case': 'nom',
                            'v': info.version
                        })

    if 'error' not in resp.json():
        for friend in resp.json()['response']['items']:
            friend['friend_of'] = member['id']
            if friend not in all_members_list:
                all_members_list.append(friend)


for i in all_members_list:
    print(i)
print(len(all_members_list))

print('-----------------')
for i in all_members_list:
    if 'friend_of' in i.keys():
        if i['friend_of']=='217033641':
            print(i)
