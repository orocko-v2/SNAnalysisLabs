import requests
import info


version = 5.199
resp = requests.get('https://api.vk.com/method/groups.getMembers',
params = {
    'access_token': info.service_key,
    'count': 500,
    'group_id': 'tomsk123',
    'sort': 'id_asc',
    'v': version
})
print('getmembers', resp.json())
member_list = resp.json()['response']['items']
print('MEMBERS', member_list)
group_list = {}
i=0
for member in member_list:
    resp = requests.get('https://api.vk.com/method/groups.get',
                        params={
                            'access_token': info.access_token,
                            'v': version,
                            'user_id': member,
                            'extended': '1',
                            'count':  1000
                        })
    print(resp.json())
    if 'error' not in resp.json():
        i+=1
        print(f'groups for member {member}', resp.json())
        groups = resp.json()['response']['items']
        print(groups)
        for group in groups:
            name = group['name']
            if group['screen_name'] !='tomsk123':
                if name not in group_list.keys():
                    group_list[name] = 1
                else:
                    group_list[name] += 1
print('----------------')
group_list = dict(sorted(group_list.items(), key=lambda item: item[1], reverse=True))
print(group_list)
print(len(group_list.keys()))
print(i)


