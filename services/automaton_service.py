import json
import uuid
import os
from fastapi import HTTPException
from schemas.dfa_schema import DFA
from schemas.dpda_schema import DPDA
from schemas.dtm_schema import DTM
from automata.fa.dfa import DFA as DFA_object
from automata.pda.dpda import DPDA as DPDA_object
from automata.tm.dtm import DTM as DTM_object
from typing import Union
from fastapi.responses import StreamingResponse

class AutomatonService():

    @staticmethod
    def create_automaton(automaton_model : Union[DTM, DPDA, DFA]) -> dict:
        """
        Cria um autômato (DFA, DPDA, DTM), gera um ID único e salva no formato JSON.
        
        Parâmetros:
        - automaton_model (Union[DTM, DPDA, DFA]): O modelo do autômato que será criado. Pode ser um objeto do tipo DTM, DPDA ou DFA.
        
        Retorna:
        - dict: Um dicionário com uma mensagem de sucesso e o ID único do autômato criado.
        
        Levanta:
        - HTTPException: Se o autômato for inválido, gerando um erro com status 400 e a mensagem correspondente.
        """
        try:
            automaton = AutomatonService.model_to_automaton(automaton_model)
            automaton.validate()
        except Exception as e:
            raise HTTPException(status_code=400, detail=f'Autômato inválido: {str(e)}')            

        if isinstance(automaton_model, DFA):
            automaton_type = "dfa"
        elif isinstance(automaton_model, DPDA):
            automaton_type = "dpda"
        elif isinstance(automaton_model, DTM):
            automaton_type = "dtm"            

        unique_id = str(uuid.uuid4())  
        file_path = f"json/{automaton_type}/{unique_id}.json"  
        automaton_data = automaton_model.dict()
        automaton_data_serializable = AutomatonService.convert_sets_to_lists(automaton_data)
        
        os.makedirs(f"json/{automaton_type}", exist_ok=True)

        with open(file_path, 'w') as file:
            json.dump(automaton_data_serializable, file, indent=4)

        return {"message": f"Autômato {automaton_type.upper()} criado com sucesso", "id": unique_id}

    @staticmethod
    def get_automaton_info(id: str, automaton_type: str) -> dict:
        """
        Recupera as informações de um autômato (DFA, DPDA, DTM) a partir do ID.
        
        Parâmetros:
        - id (str): O ID único do autômato.
        - automaton_type (str): O tipo do autômato (DFA, DPDA ou DTM).
        
        Retorna:
        - dict: Um dicionário com os dados do autômato recuperado.
        
        Levanta:
        - HTTPException: Se o autômato não for encontrado, gerando um erro com status 404 e a mensagem correspondente.
        """
        file_path = f"json/{automaton_type}/{id}.json"
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Autômato não encontrado")

        with open(file_path, 'r') as file:
            return json.load(file)
        
    @staticmethod
    def convert_sets_to_lists(automaton_data: dict):
        """
        Converte recursivamente todos os sets para listas no dicionário do autômato.
        
        Parâmetros:
        - automaton_data (dict): O dicionário contendo os dados do autômato.
        
        Retorna:
        - dict: O dicionário atualizado, com sets convertidos para listas.
        """
        if isinstance(automaton_data, dict):
            return {key: AutomatonService.convert_sets_to_lists(value) for key, value in automaton_data.items()}
        elif isinstance(automaton_data, set):
            return list(automaton_data)
        else:
            return automaton_data

    @staticmethod
    def model_to_automaton(automaton_data: Union[DTM, DPDA, DFA]):
        """
        Converte os dados JSON de um autômato em um objeto específico para simulação.
        Dependendo do tipo de autômato, um objeto correspondente será retornado (DFA, DPDA, DTM).
        
        Parâmetros:
        - automaton_data (Union[DTM, DPDA, DFA]): O modelo de autômato a ser convertido.
        
        Retorna:
        - Union[DFA_object, DPDA_object, DTM_object]: Um objeto específico para simulação (DFA, DPDA ou DTM).
        
        Levanta:
        - ValueError: Se o tipo de autômato não for válido (nem DTM, nem DPDA, nem DFA).
        """
        if not isinstance(automaton_data, (DFA, DPDA, DTM)):
            raise ValueError("Tipo de autômato inválido. Deve ser DFA, DPDA ou DTM.")

        if isinstance(automaton_data, DFA):
            dfa = DFA_object(
                states=automaton_data.states,
                input_symbols=automaton_data.input_symbols,
                transitions=automaton_data.transitions,
                initial_state=automaton_data.initial_state,
                final_states=automaton_data.final_states
            )
            return dfa
        
        elif isinstance(automaton_data, DPDA):
            dpda = DPDA_object(
                states=automaton_data.states,
                input_symbols=automaton_data.input_symbols,
                stack_symbols=automaton_data.stack_symbols,
                transitions=automaton_data.transitions,
                initial_state=automaton_data.initial_state,
                initial_stack_symbol=automaton_data.initial_stack_symbol,
                final_states=automaton_data.final_states,
                acceptance_mode=automaton_data.acceptance_mode
            )
            return dpda
        
        elif isinstance(automaton_data, DTM):
            dtm = DTM_object(
                states=automaton_data.states,
                input_symbols=automaton_data.input_symbols,
                tape_symbols=automaton_data.tape_symbols,
                transitions=automaton_data.transitions,
                initial_state=automaton_data.initial_state,
                blank_symbol=automaton_data.blank_symbol,
                final_states=automaton_data.final_states
            )
            return dtm
    
    @staticmethod
    def accept_input(automaton_data: Union[DTM, DPDA, DFA], string: str) -> dict:
        """
        Testa se uma string é aceita por um autômato (DFA, DPDA, DTM).
        
        Parâmetros:
        - automaton_data (Union[DTM, DPDA, DFA]): O modelo do autômato.
        - string (str): A string que será testada.
        
        Retorna:
        - dict: Um dicionário com a mensagem indicando se a string foi aceita ou rejeitada.
        
        Levanta:
        - HTTPException: Se o autômato não for válido ou não criado corretamente.
        """
        automaton = AutomatonService.model_to_automaton(automaton_data)
    
        if automaton is None:
            raise HTTPException(status_code=400, detail="Autômato inválido ou não criado corretamente")

        if automaton.accepts_input(string):
            return {"message": "String aceita"}
        return {"message": "String rejeitada"}

    @staticmethod 
    def show_diagram(automaton_data: Union[DFA, DPDA], id: str) -> StreamingResponse:
        """
        Exibe um diagrama de um autômato (DFA, DPDA).
        
        Parâmetros:
        - automaton_data (Union[DFA, DPDA]): O modelo do autômato que será exibido.
        - id (str): O ID único do autômato que será usado para gerar o diagrama.
        
        Retorna:
        - StreamingResponse: Uma resposta que contém o diagrama do autômato como uma imagem PNG.
        
        Levanta:
        - HTTPException: Se ocorrer um erro ao gerar o diagrama.
        """
        automaton = AutomatonService.model_to_automaton(automaton_data)

        if isinstance(automaton_data, DFA):
            automaton_type = "dfa"
        elif isinstance(automaton_data, DPDA):
            automaton_type = "dpda"
        
        image_path = f"./images/{automaton_type}/{id}.png"
        os.makedirs(f"images/{automaton_type}", exist_ok=True)
        automaton.show_diagram(path=image_path)

        return StreamingResponse(open(image_path, "rb"), media_type="image/png")
