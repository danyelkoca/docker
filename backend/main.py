from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint.
    Returns a welcome message.
    """
    return {"message": "hello"}


@app.get("/status", tags=["Status"])
def get_status():
    """
    Status endpoint.
    Returns the status of the application.
    """
    return {"status": "running"}


@app.get("/info", tags=["Info"])
def get_info():
    """
    Info endpoint.
    Returns information about the application.
    """
    return {"app": "FastAPI Example", "version": "1.0.0"}
