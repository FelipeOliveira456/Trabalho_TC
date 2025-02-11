from fastapi import APIRouter
from services.dfa_service import DFAService  
from schemas.dfa_schema import DFA
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/create", response_model=dict)
def create_dfa(dfa_data: DFA):
    """
    Cria um novo DFA a partir dos dados fornecidos pelo usuário.

    Este endpoint permite criar um novo Autômato Finito Determinístico (DFA) com base nas informações 
    fornecidas pelo usuário, como o alfabeto, estados, estado inicial e funções de transição. O serviço
    de criação é realizado pelo `DFAService`, que retorna um dicionário com os detalhes do DFA criado.

    Parâmetros:
        dfa_data (DFA): Objeto que contém os dados necessários para criar um DFA.

    Retorna:
        dict: Um dicionário com os detalhes do DFA criado, incluindo seu ID e outras informações relevantes.
    """
    return DFAService.create_dfa(dfa_data)


@router.get("/{id}", response_model=dict)
def get_dfa(id: str):
    """
    Recupera as informações detalhadas de um DFA a partir do ID fornecido.

    Este endpoint permite que o usuário recupere informações sobre um DFA existente com base no seu ID. 
    As informações retornadas incluem o alfabeto, estados, estado inicial, funções de transição, entre outras.

    Parâmetros:
        id (str): O ID do DFA que se deseja consultar.

    Retorna:
        dict: Um dicionário contendo as informações detalhadas sobre o DFA, como estados, transições e alfabeto.
    """
    return DFAService.get_dfa_info(id)


@router.post("/{id}/accept_input", response_model=dict)
def accept_input(id: str, input_string: str):
    """
    Testa se uma string de entrada é aceita por um DFA específico.

    Este endpoint permite que o usuário teste uma string de entrada em um DFA identificado pelo seu ID. 
    O serviço verifica se a string é aceita pelo autômato, retornando um resultado indicando se a string
    é aceita ou rejeitada com base nas regras de transição do DFA.

    Parâmetros:
        id (str): O ID do DFA onde a string de entrada será testada.
        input_string (str): A string de entrada que será testada no DFA.

    Retorna:
        dict: Um dicionário com o resultado do teste, indicando se a string foi aceita ou rejeitada pelo DFA.
    """
    return DFAService.accept_input(id, input_string)


@router.get("/{id}/show_diagram", response_class=StreamingResponse)
def show_diagram(id: str):
    """
    Exibe o diagrama visual de um DFA ou DPDA em formato PNG.

    Este endpoint gera e retorna um diagrama visual do DFA ou DPDA especificado pelo seu ID. O diagrama 
    é gerado no formato PNG e pode ser exibido diretamente no navegador ou em outra ferramenta de visualização.

    Parâmetros:
        id (str): O ID do DFA ou DPDA para o qual o diagrama será gerado.

    Retorna:
        StreamingResponse: A resposta contendo o diagrama do DFA ou DPDA no formato PNG.
    """
    return DFAService.show_diagram(id)
