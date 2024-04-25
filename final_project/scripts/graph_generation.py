import networkx as nx
import json
import matplotlib.pyplot as plt
class Cfg_Graph:

	def __init__(self):
		with open("../cfg_json_files/sample_out_main.json", 'r') as fd:
			self.dict = json.load(fd)
		self.cfg = self.dict['main']
		self.graph = nx.DiGraph()
		self.flow_types = [
			"CALL_OVERRIDE_UNCONDITIONAL",
			"CALL_TERMINATOR",
			"CALLOTHER_OVERRIDE_CALL",
			"CALLOTHER_OVERRIDE_JUMP",
			"COMPUTED_CALL",
			"COMPUTED_CALL_TERMINATOR",
			"COMPUTED_JUMP",
			"CONDITIONAL_CALL",
			"CONDITIONAL_CALL_TERMINATOR",
			"CONDITIONAL_COMPUTED_CALL",
			"CONDITIONAL_COMPUTED_JUMP",
			"CONDITIONAL_JUMP",
			"CONDITIONAL_TERMINATOR",
			"DATA",
			"DATA_IND",
			"EXTERNAL_REF",
			"FALL_THROUGH",
			"FLOW",
			"INDIRECTION",
			"INVALID",
			"JUMP_OVERRIDE_UNCONDITIONAL",
			"JUMP_TERMINATOR",
			"PARAM",
			"READ",
			"READ_IND",
			"READ_WRITE",
			"READ_WRITE_IND",
			"TERMINATOR",
			"THUNK",
			"UNCONDITIONAL_CALL",
			"UNCONDITIONAL_JUMP",
			"WRITE",
			"WRITE_IND"
	]

	def create_graph(self):
		# Loop through each key-value pair in the dictionary
		#for node in self.cfg:
		#	print(node)
		for source, target, flow_type in self.cfg:
			print(source, target, flow_type)
			self.graph.add_edge(source, target, label= flow_type)  # Add edge from source to target
		return self.graph
	
	def visualize_graph(self, graph):
		# Generate the visualization
		plt.figure(figsize=(100, 60))
		pos = nx.nx_agraph.graphviz_layout(self.graph, prog='dot')	# Positions for all nodes
		nx.draw(self.graph, pos, with_labels=True, node_size=700, node_color='lightblue', edge_color='gray', font_size=7)
		edge_labels = nx.get_edge_attributes(self.graph, 'label')
		nx.draw_networkx_edge_labels(self.graph, pos, edge_labels = edge_labels, font_size = 8, label_pos = 0.5, rotate=
		False)
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
cfg_obj = cfg.create_graph()
cfg.visualize_graph(cfg_obj)
