from fastapi import FastAPI

app = FastAPI(title="Agent Framework")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
