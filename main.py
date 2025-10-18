from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

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
        raise HTTPException(status_code=500, detail=str(e))

# --- NUEVO ENDPOINT ---
@app.get("/files/{file_name}")
async def get_file_content(file_name: str):
    """
    Este endpoint devuelve el contenido de un archivo específico.
    """
    file_path = os.path.join(FILES_DIRECTORY, file_name)

    if not os.path.exists(file_path):
        # Si el archivo no existe, devolvemos un error 404
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=file_path)