from services.automaton_service import AutomatonService
from schemas.dtm_schema import DTM

class DTMService(AutomatonService):

    @staticmethod
    def create_dtm(dtm_data: dict) -> dict:
        """
        Cria um DTM, valida e salva o autômato no formato JSON.
        
        Parâmetros:
        - dtm_data (dict): Um dicionário contendo os dados do DTM a ser criado. Espera-se que contenha os estados, símbolos de entrada, símbolos de fita, transições, estado inicial, símbolo em branco e estados finais.
        
        Retorna:
        - dict: Um dicionário com uma mensagem de sucesso e o ID único do DTM criado.
        
        Levanta:
        - HTTPException: Se o autômato não for válido, gerando um erro com status 400 e a mensagem correspondente.
        """
        return AutomatonService.create_automaton(dtm_data)
    
    @staticmethod
    def get_dtm_info(id: str) -> dict:
        """
        Recupera as informações de um DTM a partir do ID.
        
        Parâmetros:
        - id (str): O ID único do DTM que será recuperado.
        
        Retorna:
        - dict: Um dicionário com os dados do DTM recuperado.
        
        Levanta:
        - HTTPException: Se o DTM não for encontrado, gerando um erro com status 404 e a mensagem correspondente.
        """
        return AutomatonService.get_automaton_info(id, "dtm")
    
    @staticmethod
    def accept_input(id: str, string: str) -> dict:
        """
        Testa se uma string é aceita por um DTM.
        
        Parâmetros:
        - id (str): O ID único do DTM a ser usado para a simulação.
        - string (str): A string que será testada para ver se é aceita pelo DTM.
        
        Retorna:
        - dict: Um dicionário com a mensagem indicando se a string foi aceita ou rejeitada.
        
        Levanta:
        - HTTPException: Se ocorrer algum erro ao validar o DTM ou a entrada.
        """
        dtm_data = DTMService.get_dtm_info(id)
        return AutomatonService.accept_input(DTM(**dtm_data), string)
