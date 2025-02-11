from pydantic import BaseModel
from typing import Set, Mapping

class DFA(BaseModel):
    states: Set[str]
    input_symbols: Set[str]
    transitions: Mapping[str, Mapping[str, str]]
    initial_state: str
    final_states: Set[str]
    allow_partial: bool = True
