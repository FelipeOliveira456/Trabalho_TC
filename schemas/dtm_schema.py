from pydantic import BaseModel
from typing import Set
from automata.tm.dtm import DTMStateT, DTMTransitionsT  

class DTM(BaseModel):
    states: Set[DTMStateT]  
    input_symbols: Set[str] 
    tape_symbols: Set[str]  
    transitions: DTMTransitionsT  
    initial_state: DTMStateT  
    blank_symbol: str  
    final_states: Set[DTMStateT]  
