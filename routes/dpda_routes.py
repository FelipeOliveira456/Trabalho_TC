from fastapi import APIRouter
from services.dpda_service import DPDAService  
from schemas.dpda_schema import DPDA
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/create", response_model=dict)
def create_dpda(dpda_data: DPDA):
    """
    Cria um novo DPDA a partir dos dados fornecidos pelo usuário.

    Este endpoint permite criar um novo Autômato de Pilha Determinístico (DPDA) com base nas informações 
    fornecidas pelo usuário, como alfabeto, estados, estado inicial, funções de transição, e o alfabeto da pilha.
    O serviço de criação é realizado pelo `DPDAService`, que retorna um dicionário com os detalhes do DPDA criado.

    Parâmetros:
        dpda_data (DPDA): Objeto contendo as informações necessárias para criar o DPDA.

    Retorna:
        dict: Um dicionário com os detalhes do DPDA criado, incluindo seu ID e outras informações relevantes.
    """
    return DPDAService.create_dpda(dpda_data)


@router.get("/{id}", response_model=dict)
def get_dpda(id: str):
    """
    Recupera as informações detalhadas de um DPDA a partir do ID fornecido.

    Este endpoint permite que o usuário recupere informações sobre um DPDA existente com base no seu ID. 
    As informações retornadas incluem alfabeto, estados, estado inicial, funções de transição, alfabeto da pilha, 
    entre outros dados.

    Parâmetros:
        id (str): O ID do DPDA que se deseja consultar.

    Retorna:
        dict: Um dicionário contendo as informações detalhadas sobre o DPDA, como estados, transições e alfabeto.
    """
    return DPDAService.get_dpda_info(id)


@router.post("/{id}/accept_input", response_model=dict)
def accept_input(id: str, input_string: str):
    """
    Testa se uma string de entrada é aceita por um DPDA específico.

    Este endpoint permite que o usuário teste uma string de entrada em um DPDA identificado pelo seu ID. 
    O serviço verifica se a string é aceita pelo autômato, retornando um resultado indicando se a string
    é aceita ou rejeitada com base nas regras de transição do DPDA.

    Parâmetros:
        id (str): O ID do DPDA onde a string de entrada será testada.
        input_string (str): A string de entrada que será testada no DPDA.

    Retorna:
        dict: Um dicionário com o resultado do teste, indicando se a string foi aceita ou rejeitada pelo DPDA.
    """
    return DPDAService.accept_input(id, input_string)


@router.get("/{id}/show_diagram", response_class=StreamingResponse)
def show_diagram(id: str):
    """
    Exibe o diagrama visual de um DPDA em formato PNG.

    Este endpoint gera e retorna um diagrama visual do DPDA especificado pelo seu ID. O diagrama 
    é gerado no formato PNG e pode ser exibido diretamente no navegador ou em outra ferramenta de visualização.

    Parâmetros:
        id (str): O ID do DPDA para o qual o diagrama será gerado.

    Retorna:
        StreamingResponse: A resposta contendo o diagrama do DPDA no formato PNG.
    """
    return DPDAService.show_diagram(id)
