from services.automaton_service import AutomatonService
from schemas.dfa_schema import DFA
from fastapi.responses import StreamingResponse


class DFAService(AutomatonService):

    @staticmethod
    def create_dfa(dfa_data: dict) -> dict:
        """
        Cria um DFA, valida e salva o autômato no formato JSON.
        
        Parâmetros:
        - dfa_data (dict): Um dicionário contendo os dados do DFA a ser criado. Espera-se que contenha os estados, símbolos de entrada, transições, estado inicial e estados finais.
        
        Retorna:
        - dict: Um dicionário com uma mensagem de sucesso e o ID único do DFA criado.
        
        Levanta:
        - HTTPException: Se o autômato não for válido, gerando um erro com status 400 e a mensagem correspondente.
        """
        return AutomatonService.create_automaton(dfa_data)
    
    @staticmethod
    def get_dfa_info(id: str) -> dict:
        """
        Recupera as informações de um DFA a partir do ID.
        
        Parâmetros:
        - id (str): O ID único do DFA que será recuperado.
        
        Retorna:
        - dict: Um dicionário com os dados do DFA recuperado.
        
        Levanta:
        - HTTPException: Se o DFA não for encontrado, gerando um erro com status 404 e a mensagem correspondente.
        """
        return AutomatonService.get_automaton_info(id, "dfa")
    
    @staticmethod
    def accept_input(id: str, string: str) -> dict:
        """
        Testa se uma string é aceita por um DFA.
        
        Parâmetros:
        - id (str): O ID único do DFA a ser usado para a simulação.
        - string (str): A string que será testada para ver se é aceita pelo DFA.
        
        Retorna:
        - dict: Um dicionário com a mensagem indicando se a string foi aceita ou rejeitada.
        
        Levanta:
        - HTTPException: Se ocorrer algum erro ao validar o DFA ou a entrada.
        """
        dfa_data = DFAService.get_dfa_info(id)
        return AutomatonService.accept_input(DFA(**dfa_data), string)
    
    @staticmethod
    def show_diagram(id: str) -> StreamingResponse:
        """
        Exibe um diagrama de um DFA.
        
        Parâmetros:
        - id (str): O ID único do DFA que será usado para gerar o diagrama.
        
        Retorna:
        - StreamingResponse: Uma resposta que contém o diagrama do DFA como uma imagem PNG.
        
        Levanta:
        - HTTPException: Se ocorrer um erro ao gerar o diagrama.
        """
        dfa_data = DFAService.get_dfa_info(id)
        return AutomatonService.show_diagram(DFA(**dfa_data), id)
