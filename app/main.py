from fastapi import FastAPI

# Inicializa a aplicação
app = FastAPI()

@app.get("/")
def leitura_raiz():
    return {"mensagem": "Olá, esta é uma API simples!"}

@app.get("/saudar/{nome}")
def saudar_usuario(nome: str):
    return {"mensagem": f"Olá, {nome}!", "status": "sucesso"}