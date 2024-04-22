from ghidra.util.graph import DirectedGraph
from ghidra.util.graph import Edge
from ghidra.util.graph import Vertex
from ghidra.util.task import * 
from ghidra.program.model.block import *
from ghidra.program.model.symbol import * 
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
		block_iter = model.getCodeBlocksContaining(self.func.getBody(), monitor) 	
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
				callers['name'] = bb_caller.getSourceBlock().getName()
				callers['start']= bb_caller.getSourceAddress().getOffset()
				#callers['end']= bb_caller.getMaxAddress().getOffset()
			#	callers['inst'] = self.prog.getListing().getInstructions(bb_caller, True)
				block['callers'].append(callers)
				block['edges'].append((bb_caller.getSourceBlock().getName(), bb.getName()))
			block['callees'] = []
			block['edges_callees'] = []
			bb_callees = bb.getDestinations(monitor)
			while bb_callees.hasNext():
				bb_callee = bb_callees.next()
				callees = {}
				callees['name'] = bb_callee.getDestinationBlock().getName()
				callees['start']= bb_callee.getDestinationAddress().getOffset()
#				callees['end']= bb_callee.getMaxAddress().getOffset()
			#	callees['inst'] = self.prog.getListing().getInstructions(bb_callee, True)
				block['callees'].append(callees)
				block['edges_callees'].append((bb.getName(), bb_callee.getDestinationBlock().getName()))	
		
			print(block)
			return block
		
#		def store_cfg(self):
def getAddress(offset):
    return currentProgram.getAddressFactory().getDefaultAddressSpace().getAddress(offset)			
prog = getCurrentProgram()
f_addr = getAddress(0x0010146b) 
f = prog.getFunctionManager().getFunctionAt(f_addr)

cfg = CFG(f)
cfg_blocks = cfg.get_basic_blocks()
