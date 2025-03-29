from fastapi import FastAPI
from pydantic import BaseModel
import hmac
import hashlib

app = FastAPI()

class SignRequest(BaseModel):
    timestamp: int
    secret: str

@app.post("/sign")
def sign(data: SignRequest):
    message = f"timestamp={data.timestamp}".encode()
    secret_bytes = data.secret.encode()
    signature = hmac.new(secret_bytes, message, hashlib.sha256).hexdigest()
    return {"signature": signature}
