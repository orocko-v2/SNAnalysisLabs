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
    'count': 10,
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


resp = requests.get('https://api.vk.com/method/groups.get',
                        params={
                            'access_token': info.service_key,
                            'v': info.version,
                            'user_id': '217033641',
                            'extended': '1',
                            'count': 5
                        })
group_list = resp.json()['response']['items']
group_dict = {}
print("group_list", group_list)
for member in all_members_list:
    print(member)
    resp = requests.get('https://api.vk.com/method/groups.get',
                        params={
                            'access_token': info.service_key,
                            'v': info.version,
                            'user_id': member['id'],
                            'extended': '1',
                            'count': 20
                        })
    if 'error' in resp.json():
        continue

    for group in resp.json()['response']['items']:
        if group in group_list:
            if group['id'] in group_dict:
                group_dict[group['id']]['count'] = group_dict[group['id']]['count'] + 1
                group_dict[group['id']]['subscribers'].append(member['id'])
            else:
                group_dict[group['id']] = {'count':  1, 'name': group['name'], 'subscribers': [member['id']]}

print('ALALALALAL GROUPS')

print(len(all_members_list))
print( {k: v for k, v in sorted(group_dict.items(), key=lambda item: item[1]['count'], reverse=True)})
print('-----------------')
for i in all_members_list:
    if 'friend_of' in i.keys():
        if i['friend_of']=='217033641':
            print(i)

print('FINAL')
interested_keys = {'id', 'first_name', 'last_name', 'friend_of'}
for d in all_members_list:
    print({k: v for k, v in d.items() if k in interested_keys})
