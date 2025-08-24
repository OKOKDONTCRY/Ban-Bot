# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Define expected request format
class BanRequest(BaseModel):
    roblox_user_id: int
    reason: str

@app.post("/api/ban")
async def ban_user(data: BanRequest):
    # Simulate ban logic or send to Roblox DataStore
    print(f"Banning Roblox user ID {data.roblox_user_id} for reason: {data.reason}")
    
    # Return success response
    return {"status": "success", "user_id": data.roblox_user_id}
