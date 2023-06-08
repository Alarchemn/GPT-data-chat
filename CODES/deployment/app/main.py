from fastapi import FastAPI
from typing import Dict
from http import HTTPStatus
from app.pre.pipe import agent
from app.pre.pipe import __version__ as chat_bot_version

# Create a FastAPI application instance
app = FastAPI()

# Format the response data with the appropriate structure
def format_response(data):
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": data
    }
    return response

# Define the response data for the home endpoint
@app.get("/")
def home() -> Dict:
    data = {
        "Chat Bot Version": chat_bot_version
    }
    response = format_response(data)
    return response

# Call the agent with the provided prompt
@app.post("/prompt/", status_code=201)
async def make_prompt(prompt: str):
    results = agent(prompt)
    response = format_response(results)
    return response
