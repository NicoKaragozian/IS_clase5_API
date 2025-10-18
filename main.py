from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def prueba_root():
    return {"message": "Accediste al endpoint de prueba"}
