from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# TODO: Defina seu modelo Pydantic para Livro aqui


# TODO: Inicialize a aplicação FastAPI


# TODO: Implemente seus endpoints aqui
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Biblioteca"}


# TODO: Adicione mais endpoints conforme necessário