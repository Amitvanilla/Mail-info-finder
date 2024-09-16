from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.openai_service import get_openai_response
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class RequestBody(BaseModel):
    prompt: str

@app.post("/generate/")
async def generate_description(request_body: RequestBody):
    prompt = request_body.prompt
    print(prompt) 
    try:
        response = await get_openai_response(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
