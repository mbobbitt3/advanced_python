from ghidra.util.graph import DirectedGraph
from ghidra.util.graph import Edge
from ghidra.util.graph import Vertex
from ghidra.util.task import * 
from ghidra.program.model.block import *
from ghidra.program.model.symbol import * 
import json
from collections import OrderedDict
class CFG:
	def __init__(self, offset):
		"""f is going to be Ghidra function object which we want the CFG for"""
		self.cfg= OrderedDict() 
		self.prog = getCurrentProgram()
		self._func = self.func_conv(offset)
	
	@property
	def func(self):
		return self._func

	@func.setter
	def func(self, offset):
		self._func = self.func_conv(offset)

	def func_conv(self, offset):
		'''this method converts a raw hex address input into a Ghidra address object
		and then gets the function object contianing that address''' 
		f_addr = self.prog.getAddressFactory().getDefaultAddressSpace().getAddress(offset)			
		f = self.prog.getFunctionManager().getFunctionContaining(f_addr)
		return f

	def gen_cfg_dict(self):
		'''get all basic blocks and callee basic blocks within function and store as pairs representing (caller, callee)
		into a dictionary that we will use to make the graph'''
		monitor = ConsoleTaskMonitor()
		model = SimpleBlockModel(self.prog) 
		block_iter = model.getCodeBlocksContaining(self._func.getBody(), monitor) 	
		f_name  = self._func.getName()
		edge_map= OrderedDict()
		edge_map[f_name] = []
		bb = block_iter.next()
		while block_iter.hasNext():
			bb_name = bb.getName()
			bb_name = bb_name.strip('lAB_')
		#	block['instructions'] = self.prog.getListing().getInstructions(bb,True) 
			bb_dests = bb.getDestinations(monitor)
			bb_succ = bb_dests.next()
			while bb_dests.hasNext():
				bb_succ_name = str(bb_succ).split('> ')[-1]
				edge_map[f_name].append((bb_name, bb_succ_name))
				bb_succ = bb_dests.next()

			bb = block_iter.next()

		return edge_map

	def save_cfg(self):
		'''conjoin elements witin kwords to make file name and then write to json output for graphing'''
		kwords = [self.prog.getName().replace('.','_'), self._func.getName()]
		out_name = '_'.join(kwords)
		cfg_dict = self.gen_cfg_dict()
		print(cfg_dict)
		with open('cfg_json_files/' + out_name + '.json', 'w+') as fd:
			json.dump(cfg_dict, fd)

cfg = CFG(0x0010146b)
cfg.save_cfg()
