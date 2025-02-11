from fastapi import APIRouter
from services.dtm_service import DTMService  
from schemas.dtm_schema import DTM

router = APIRouter()

@router.post("/create", response_model=dict)
def create_dtm(dtm_data: DTM):
    """
    Cria um novo DTM a partir dos dados fornecidos.

    Este endpoint permite criar um novo Máquina de Turing Determinística (DTM) com base nas informações 
    fornecidas pelo usuário, como alfabeto, estados, estado inicial, funções de transição e a fita de entrada.
    O serviço de criação é realizado pelo `DTMService`, que retorna um dicionário com os detalhes do DTM criado.

    Parâmetros:
        dtm_data (DTM): Objeto contendo as informações necessárias para criar o DTM.

    Retorna:
        dict: Um dicionário com os detalhes do DTM criado, incluindo seu ID e outras informações relevantes.
    """
    return DTMService.create_dtm(dtm_data)


@router.get("/{id}", response_model=dict)
def get_dtm(id: str):
    """
    Recupera as informações detalhadas de um DTM a partir do ID fornecido.

    Este endpoint permite que o usuário recupere informações sobre um DTM existente com base no seu ID. 
    As informações retornadas incluem alfabeto, estados, estado inicial, funções de transição, e outras propriedades.

    Parâmetros:
        id (str): O ID do DTM que se deseja consultar.

    Retorna:
        dict: Um dicionário contendo as informações detalhadas sobre o DTM, como estados, transições e alfabeto.
    """
    return DTMService.get_dtm_info(id)


@router.post("/{id}/accept_input", response_model=dict)
def accept_input(id: str, input_string: str):
    """
    Testa se uma string de entrada é aceita por um DTM específico.

    Este endpoint permite que o usuário teste uma string de entrada em um DTM identificado pelo seu ID. 
    O serviço verifica se a string é aceita pelo DTM, retornando um resultado indicando se a string
    é aceita ou rejeitada com base nas regras de transição do DTM.

    Parâmetros:
        id (str): O ID do DTM onde a string de entrada será testada.
        input_string (str): A string de entrada que será testada no DTM.

    Retorna:
        dict: Um dicionário com o resultado do teste, indicando se a string foi aceita ou rejeitada pelo DTM.
    """
    return DTMService.accept_input(id, input_string)
