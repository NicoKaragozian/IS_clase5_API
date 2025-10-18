import os
from fastapi import FastAPI

app = FastAPI()

# Directorio donde se guardarán los archivos
FILES_DIRECTORY = "./files"

# Asegurarse de que el directorio exista
os.makedirs(FILES_DIRECTORY, exist_ok=True)


@app.get("/files")
async def list_files():
    """
    Este endpoint devuelve una lista de los archivos
    disponibles en el servidor.
    """
    try:
        files = os.listdir(FILES_DIRECTORY)
        return {"files": files}
    except Exception as e:
        return {"error": str(e)}