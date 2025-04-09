import os

import litellm
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    model: str = "gpt-3.5-turbo"  # Default model
    prompt: str
    temperature: float = 0.7
    max_tokens: int = 256


@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.post("/chat/")
async def chat(request: ChatRequest):
    try:
        # Call OpenAI using litellm
        response = litellm.completion(
            api_base=LLM_PROVIDER_BASE,
            api_key=LLM_API_TOKEN,
            model=request.model,
            messages=[{"role": "user", "content": request.prompt}],
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )

        return {"response": response["choices"][0]["message"]["content"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
