from fastapi import FastAPI

app = FastAPI(title="Academia de Natación")


@app.get("/health")
def health():
    return {"status": "ok"}
