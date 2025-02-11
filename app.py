from fastapi import FastAPI
from routes.dfa_routes import router as dfa_router
from routes.dpda_routes import router as dpda_router
from routes.dtm_routes import router as dtm_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

app = FastAPI(
    title="API de Autômatos",
    description="Esta API fornece endpoints para interagir com diferentes modelos de autômatos como DFA, DPDA e DTM.",
    version="1.0.0",
    contact={
        "name": "Felipe Oliveira",
    }
)

app.include_router(dfa_router, prefix="/dfa", tags=["DFA"])
app.include_router(dpda_router, prefix="/dpda", tags=["DPDA"])
app.include_router(dtm_router, prefix="/dtm", tags=["DTM"])

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Endpoint principal que renderiza a página inicial.

    Este endpoint retorna uma página HTML que serve como a página principal
    da API de Autômatos. Ela é renderizada usando templates do Jinja2.

    Retorna:
        HTMLResponse: A página HTML renderizada com o template.
    """
    return templates.TemplateResponse("index.html", {"request": request})
