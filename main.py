from fastapi import FastAPI

app = FastAPI()

#dfgre
@app.get("/trigger-endpoint")
def trigger_endpoint():
    return {"message": "Endpoint triggered successfully!"}
