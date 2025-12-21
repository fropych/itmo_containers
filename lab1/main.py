import uuid
import os

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    
    
    os.makedirs("/app/data", exist_ok=True)
    filename = f"/app/data/{uuid.uuid4()}.txt"
    with open(filename, "w") as f:
        f.write("Hello from persistent volume!")
        
    return {"message": "Hello World", "file_created": filename}
