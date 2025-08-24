from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Temporary in-memory ban list
banned_users = {}

# Root route to fix Render 404
@app.get("/")
async def root():
    return {"message": "Ban API is running successfully."}

# Optional favicon route to stop browser 404s
@app.get("/favicon.ico")
async def favicon():
    return {}

# Schema for ban request
class BanRequest(BaseModel):
    roblox_user_id: int
    reason: str

# Ban a user (POST)
@app.post("/api/ban")
async def ban_user(data: BanRequest):
    banned_users[data.roblox_user_id] = data.reason
    return {"status": "success", "user_id": data.roblox_user_id, "reason": data.reason}

# Check if user is banned (GET)
@app.get("/api/ban/{user_id}")
async def check_ban(user_id: int):
    if user_id in banned_users:
        return {"banned": True, "reason": banned_users[user_id]}
    return {"banned": False}

# Run locally (optional)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
