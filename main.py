import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class File(BaseModel):
    name: str
    content: str

# Endpoint 1: Listar archivos
@app.get("/files")
async def list_files():
    return {"files": os.listdir("./files")}

# Endpoint 2: Ver el contenido de un archivo
@app.get("/files/{file_name}")
async def get_file_content(file_name: str):
    with open(f"./files/{file_name}", "r", encoding="utf-8") as f:
        content = f.read()
    return {"content": content}

# Endpoint 3: Crear un archivo
@app.post("/files")
async def create_file(file: File):
    with open(f"./files/{file.name}", "w", encoding="utf-8") as f:
        f.write(file.content)
    return {"message": f"Archivo '{file.name}' creado."}