from services.automaton_service import AutomatonService
from schemas.dpda_schema import DPDA
from fastapi.responses import StreamingResponse


class DPDAService(AutomatonService):

    @staticmethod
    def create_dpda(dpda_data: dict) -> dict:
        """
        Cria um DPDA, valida e salva o autômato no formato JSON.
        
        Parâmetros:
        - dpda_data (dict): Um dicionário contendo os dados do DPDA a ser criado. Espera-se que contenha os estados, símbolos de entrada, símbolos de pilha, transições, estado inicial, símbolo inicial de pilha e estados finais.
        
        Retorna:
        - dict: Um dicionário com uma mensagem de sucesso e o ID único do DPDA criado.
        
        Levanta:
        - HTTPException: Se o autômato não for válido, gerando um erro com status 400 e a mensagem correspondente.
        """
        return AutomatonService.create_automaton(dpda_data)
    
    @staticmethod
    def get_dpda_info(id: str) -> dict:
        """
        Recupera as informações de um DPDA a partir do ID.
        
        Parâmetros:
        - id (str): O ID único do DPDA que será recuperado.
        
        Retorna:
        - dict: Um dicionário com os dados do DPDA recuperado.
        
        Levanta:
        - HTTPException: Se o DPDA não for encontrado, gerando um erro com status 404 e a mensagem correspondente.
        """
        return AutomatonService.get_automaton_info(id, "dpda")
    
    @staticmethod
    def accept_input(id: str, string: str) -> dict:
        """
        Testa se uma string é aceita por um DPDA.
        
        Parâmetros:
        - id (str): O ID único do DPDA a ser usado para a simulação.
        - string (str): A string que será testada para ver se é aceita pelo DPDA.
        
        Retorna:
        - dict: Um dicionário com a mensagem indicando se a string foi aceita ou rejeitada.
        
        Levanta:
        - HTTPException: Se ocorrer algum erro ao validar o DPDA ou a entrada.
        """
        dpda_data = DPDAService.get_dpda_info(id)
        return AutomatonService.accept_input(DPDA(**dpda_data), string)
    
    @staticmethod
    def show_diagram(id: str) -> StreamingResponse:
        """
        Exibe um diagrama de um DPDA.
        
        Parâmetros:
        - id (str): O ID único do DPDA que será usado para gerar o diagrama.
        
        Retorna:
        - StreamingResponse: Uma resposta que contém o diagrama do DPDA como uma imagem PNG.
        
        Levanta:
        - HTTPException: Se ocorrer um erro ao gerar o diagrama.
        """
        dpda_data = DPDAService.get_dpda_info(id)
        return AutomatonService.show_diagram(DPDA(**dpda_data), id)
