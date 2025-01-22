from statistics import median
import requests

import info

version = info.version

def doLab2(return_type, count):
    print('lab1.2')
    resp = requests.get('https://api.vk.com/method/groups.getMembers',
                        params={
                            'access_token': info.service_key,
                            'count': count,
                            'group_id': 'tomsk123',
                            'sort': 'id_asc',
                            'v': version
                        })

    member_list = resp.json()['response']['items']
    member_count = len(member_list)
    sum_age = 0
    return_list =[]
    age_list = []
    sex_dict = {'male': 0, "female": 0, "na": 0}
    city_dict = {}
    for member in member_list:
        print(member)
        resp = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': info.service_key,
                                'user_ids': member,
                                'fields': 'bdate, sex, city, country, is_closed',
                                'name_case': 'nom',
                                'v': version,
                            })
        if resp.json()['response'][0]['is_closed'] or 'deactivated' in resp.json()['response'][0].keys():
            member_count -= 1
            continue
        return_list.append(resp.json()['response'][0])
        print(resp.json()['response'][0])
        if not resp.json()['response'][0].get('bdate'):
            age = 0
        elif len(resp.json()['response'][0]['bdate']) != 9 and len(resp.json()['response'][0]['bdate']) != 10:
            age = 0
        else:
            age = 2024 - int(resp.json()['response'][0]['bdate'][-4:])
            sum_age += age
        age_list.append(age)
        if (resp.json()['response'][0].get('sex')):
            match resp.json()['response'][0]['sex']:
                case 0:
                    sex_dict['na'] += 1
                case 1:
                    sex_dict['female'] += 1
                case 2:
                    sex_dict['male'] += 1

        if (resp.json()['response'][0].get('city')):
            city_name = resp.json()['response'][0]['city']['title']
            if city_name in city_dict.keys():
                city_dict[city_name] += 1
            else:
                city_dict[city_name] = 1
        else:
            if 'NA' in city_dict.keys():
                city_dict['NA'] += 1
            else:
                city_dict['NA'] = 1

    print(len([age for age in age_list if age != 0]))
    average_age = sum(age for age in age_list if age != 0) / len([age for age in age_list if age != 0])
    median_age = median([age for age in age_list if age != 0])
    unknown_age = len([age for age in age_list if age == 0]) / member_count * 100
    male_perc = sex_dict['male'] / member_count * 100
    female_perc = sex_dict['female'] / member_count * 100
    na_perc = sex_dict['na'] / member_count * 100

    print(member_count)
    print('average_age=', average_age)
    print('median_age=', median_age)
    print('unknown_age=', unknown_age)
    print('male_perc=', male_perc)
    print('female_perc=', female_perc)
    print('na_perc=', na_perc)

    for key, value in sorted(city_dict.items(), key=lambda x: x[1], reverse=True):
        print("{} : {}".format(key, value))

    if return_type == 'users':
        return return_list
    elif return_type == 'cities':
        return city_dict
    else:
        return (return_list, city_dict)





