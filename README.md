# Trabalho de Teoria da Computação

Este projeto utiliza a biblioteca Python Automata em conjunto com o FastAPI para construir uma API eficiente e de alto desempenho, permitindo a criação, recuperação, visualização e teste de autômatos finitos determinísticos (DFA), máquinas de Turing determinísticas (DTM) e autômatos de pilha determinísticos (DPDA).

## Descrição

A API oferece os seguintes endpoints para interação com os autômatos:

- **POST /{tipo}/create**: Cria um novo autômato do tipo especificado (DFA, DTM ou DPDA).
- **GET /{tipo}/{id}**: Recupera um autômato existente pelo seu ID.
- **GET /{tipo}/{id}/show_diagram**: Gera e retorna um diagrama visual do autômato.
- **POST /{tipo}/{id}/accept_input**: Testa uma string de entrada no autômato especificado.

A captura de dados é realizada por meio de JSON, e a recuperação do autômato retorna um JSON representando o autômato.

## Estrutura de Diretórios

A estrutura de diretórios do projeto é organizada da seguinte forma:

```
Trabalho_TC/
├── routes/        # Contém os arquivos de definição dos endpoints da API
├── services/      # Contém a lógica de negócios e manipulação dos autômatos
├── schemas/       # Contém os esquemas Pydantic para validação de dados
├── images/        # Armazena os diagramas visuais dos autômatos
├── json/          # Armazena os arquivos JSON dos autômatos
├── static/        # Arquivos estáticos servidos pela aplicação
└── templates/     # Templates HTML para renderização de páginas
```


## Tecnologias Utilizadas

- **Python 3.11+**: Linguagem de programação principal.
- **FastAPI**: Framework web para construção de APIs rápidas e eficientes.
- **Automata-lib**: Biblioteca para manipulação e simulação de autômatos.
- **Uvicorn**: Servidor ASGI para execução da aplicação.

## Comandos para configurar o ambiente


1. Clone o repositorio
```bash
git clone git@github.com:FelipeOliveira456/Trabalho_TC.git
```
2. Acesse o diretório do projeto
```bash
cd Trabalho_TC
```
3. Crie um ambiente virtual e o ative
```bash
python -m venv venv
source venv/bin/activate 
```
4. Instale graphviz para a visualização gráfica do autômato
```bash
sudo apt install libgraphviz-dev
```
5. Instale os requisitos
```bash
pip install -r requirements.txt
```

## Uso

1. Execute no terminal o comando para criar o servidor
```bash
uvicorn app:app --reload
```
2. Abra em algum navegador
```
localhost:8000
```

## Documentação

Visualize a documentação em 
```
localhost:8000/docs
```
 
## Testes

As instâncias para testes estão no diretório tests e contém uma instância JSON para cada autômato. 

As instâncias foram retiradas da documentação oficial da biblioteca automata.

## Referências

https://caleb531.github.io/automata/

https://fastapi.tiangolo.com/

https://www.uvicorn.org/


