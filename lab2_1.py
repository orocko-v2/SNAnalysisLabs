from pyvis.network import Network
import random
r = lambda: random.randint(0,255)
import lab1_2

group_users_graph = Network(notebook=True)
group_users_graph.show_buttons(filter_=True)
group_users_graph.repulsion(node_distance=100, spring_length=150)

users = lab1_2.doLab2()

group_users_graph.add_node(
    1,
    label='Group',
    title = 'Регион-70 | Томск',
    color = '#1818c7'
)

group_users_graph.add_nodes(
    [el['id'] for el in users],
    label = ['User'] * len(users),
    title = [str(el['first_name'] + ' ' + el['last_name']) for el in users],
    color = ['#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))]*len(users)
)
group_users_graph.add_edges([(1, el['id']) for el in users])
group_users_graph.show('graph1.html')

