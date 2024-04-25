import matplotlib.pyplot as plt
import networkx as nx
def dot_to_nx_graph():

	with open('../sample/sample_out_main.dot', 'r') as dot:
		data = dot.read().splitlines()

		# process dot files into networkx graph
		G = nx.DiGraph()
		func_name = data[0].split('"')[1]

		entry_node = None
		exit_node = None

		for line in data[1:]:
			if '->' in line:
				nodes = line.split('->')
				s = nodes[0].strip('"')
				e = nodes[1].strip('"').strip(';').strip('"')


			elif '=' in line:
				entry_node = line.split('entry: ')[-1].split(',')[0]
				exit_node = line.split('exit: ')[-1].rstrip('"')

			G.add_node(s)
			G.add_edge(s, e)

	plt.figure(figsize=(10, 6))
	pos = nx.nx_pydot.graphviz_layout(G, scale=3)# Type of graph we want to ue
	nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', edge_color='gray', font_size=6)
	plt.title("Control Flow Graph")
	plt.show()	# Display the graph

dot_to_nx_graph()
