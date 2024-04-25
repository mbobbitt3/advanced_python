import networkx as nx
import json
import matplotlib.pyplot as plt
class Cfg_Graph:

	def __init__(self):
		with open("../cfg_json_files/sample_out_main.json", 'r') as fd:
			self.dict = json.load(fd)
		self.cfg = self.dict['main']
		self.graph = nx.DiGraph(self.cfg)

	def create_graph(self, flow_dict):
		# Loop through each key-value pair in the dictionary
		for source, targets in self.cfg.items():
			for target in targets:
				self.graph.add_edge(source, target)  # Add edge from source to target

	def visualize_graph(self):
		# Generate the visualization
		plt.figure(figsize=(10, 6))
		pos = nx.spring_layout(self.graph)	# Positions for all nodes
		nx.draw(self.graph, pos, with_labels=True, node_size=700, node_color='lightblue', edge_color='gray', font_size=10)
		plt.title("Control Flow Graph")
		plt.show()	# Display the graph
	
	'''
	def make_graph(self):
		self.graph.add_edges_from(self.cfg)
		pos = nx.spring_layout(self.graph)
		nx.draw_networkx(self.graph, with_labels = True)
		plt.show()
	'''
cfg = Cfg_Graph()
cfg.visualize_graph()

