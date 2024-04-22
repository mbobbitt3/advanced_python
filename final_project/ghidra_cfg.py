from ghidra.util.graph import DirectedGraph
from ghidra.util.graph import Edge
from ghidra.util.graph import Vertex
from ghidra.program.model.block import *
from collections import OrderedDict
class CFG:
	def __init__(self, f):
		"""f is going to be Ghidra function object which we want the CFG for"""
		self.blocks= [] 
		self.func = f
		self.prog = getCurrentProgram()
	
	def get_basic_blocks(self):
		monitor = ConsoleTaskMonitor()
		model = SimpleBlockModel(self.prog) 
		block_iter = model.getCodeBlocksContaining(self.f.getBody(), monitor) 	
		while block_iter.hasNext():
			bb = block_iter.next()
			block = OrderedDict()
			block['name'] = bb.getName()
			block['start'] = bb.getFirstStartAddress().getOffset()
			block['end'] = bb.getMaxAddress().getOffset()
		#	block['instructions'] = self.prog.getListing().getInstructions(bb,True) 
			block['callers'] = [] 
			block['edges'] = []
			bb_callers = bb.getSources(monitor)
			while bb_callers.hasNext():
				bb_caller = bb_callers.next()
				callers = {}
				callers['name'] = bb_caller.getName()
				callers['start']= bb_caller.getFirstStartAddress().getOffset()
				callers['end']= bb_caller.getMaxAddress().getOffset()
			#	callers['inst'] = self.prog.getListing().getInstructions(bb_caller, True)
				block['callers'].append(callers)
				block['edges'].append(bb_caller.getName(), bb.getName())
			block['callees '] = []
			bb_callees = bb.getDestinations(monitor)
			while bb_callees.hasNext():
				bb_callee = bb_callees.next()
				callees = {}
				callees['name'] = bb_callee.getName()
				callees['start']= bb_callee.getFirstStartAddress().getOffset()
				callees['end']= bb_callee.getMaxAddress().getOffset()
			#	callees['inst'] = self.prog.getListing().getInstructions(bb_callee, True)
				block['callees'].append(callees)
				block['edges_callees'].append(bb.getName(), bb_callee.getName())	
		
			print(blocks)
			return blocks
		
		def store_cfg(self):
			
prog = getCurrentProgram()

