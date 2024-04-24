from ghidra.util.graph import DirectedGraph
from ghidra.util.graph import Edge
from ghidra.util.graph import Vertex
from ghidra.util.task import * 
from ghidra.program.model.block import *
from ghidra.program.model.symbol import * 
from collections import OrderedDict
class CFG:
	def __init__(self):
		"""f is going to be Ghidra function object which we want the CFG for"""
		self.blocks= [] 
		self.prog = getCurrentProgram()
	
	def get_basic_blocks(self, f):
		dot_name = [self.prog.getName().replace('.','_'), f.getName()]
		dot_name = '_'.join(dot_name)
		dot_f = open('../' + dot_name + '.dot', 'w+')
		out = "digraph" + '"' + f.getName() + '"' + "{"
		dot_f.write(out + '\n')
		monitor = ConsoleTaskMonitor()
		model = SimpleBlockModel(self.prog) 
		block_iter = model.getCodeBlocksContaining(f.getBody(), monitor) 	
		bb = block_iter.next()
		node_enter = None
		node_exit  = None
		while block_iter.hasNext():
			succ_bbs = bb.getDestinations(monitor) #get callees of basic block
			while succ_bbs.hasNext():
				block = OrderedDict()
				bb_name = bb.getName()
#				bb_name = bb_name[0]
				bb_name = bb_name.strip('LAB_')
				bb_start = bb.getFirstStartAddress().getOffset()
				bb_end = bb.getMaxAddress().getOffset()
				bb_succ = succ_bbs.next()
			#	block['instructions'] = self.prog.getListing().getInstructions(bb,True) 
			#	bb_succ_name = bb_succ.getName()
			#	bb_succ_start = bb_succ.getFirstStartAddress().getOffset()
				bb_succ_name = str(bb_succ).split('> ')[-1]
				if not node_enter:
					node_enter = bb_name

				node_exit = bb_succ_name
				dot_f.write('"' + bb_name + '"' + "->" + '"' + bb_succ_name + '"' + ";\n")

				print('"' + bb_name + '"' + "->" + '"' + bb_succ_name + '"')

			bb = block_iter.next()
	
		if node_enter and node_exit:
			n_entry = "entry: {}, ".format(node_enter)
			n_exit = "exit {}".format(node_exit)
			dot_f.write('comment: "{}{}"\n'.format(n_entry, n_exit))
		
		dot_f.write('}\n')
		dot_f.close()
		
	def get_func(self, offset):
		f_addr = self.prog.getAddressFactory().getDefaultAddressSpace().getAddress(offset)			
		f = self.prog.getFunctionManager().getFunctionAt(f_addr)
		return f

cfg = CFG()
f = cfg.get_func(0x0010146b) 
cfg_blocks = cfg.get_basic_blocks(f)
