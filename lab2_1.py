from pyvis.network import Network
import random
r = lambda: random.randint(0,255)
import lab1_2

group_users_graph = Network(notebook=True)
group_users_graph.show_buttons(filter_=True)
group_users_graph.repulsion(node_distance=100, spring_length=150)
color_map = {
    1: '#FFB6C1',
    2: '#4169E1'
}

data = lab1_2.doLab2('all')
users = data[0]
cities = data[1]
del cities['NA']

get_colors = lambda n: ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(n)]
get_colors(3)

cities_list = list(range(1, len(cities)+1))
group_users_graph.add_nodes(
    list(range(1, len(cities)+1)),
    label=list(cities.keys()),
    title = list(cities.keys()),
    color = get_colors(len(cities)),
    shape = ['box']*len(cities)
)

group_users_graph.add_nodes(
    [el['id'] for el in users],
    label = [el['first_name'] for el in users],
    title = [str(el['first_name'] + ' ' + el['last_name']) for el in users],
    color = [color_map[el['sex']] for el in users]
)

for user in users:
    for city in cities_list:
        if user.get('city'):
            if group_users_graph.get_node(city)['title'] == user['city']['title']:
                group_users_graph.add_edge(city, user['id'])

for edge in group_users_graph.get_edges():
    edge['color'] = 'black'
group_users_graph.show('graph1.html')

