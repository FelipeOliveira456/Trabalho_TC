from pydantic import BaseModel
from typing import Set
from automata.pda.dpda import DPDATransitionsT, DPDAStateT
from automata.pda.pda import PDAAcceptanceModeT

class DPDA(BaseModel):
    states: Set[DPDAStateT]  
    input_symbols: Set[str]  
    stack_symbols: Set[str]
    transitions: DPDATransitionsT  
    initial_state: DPDAStateT  
    initial_stack_symbol: str  
    final_states: Set[DPDAStateT]  
    acceptance_mode: PDAAcceptanceModeT  
