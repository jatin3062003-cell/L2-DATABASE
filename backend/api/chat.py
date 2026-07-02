from fastapi import APIRouter
from pydantic import BaseModel

from main import ask_agent

router = APIRouter(
    prefix="/chat",
    tags=["AI Assistant"]
)


class ChatRequest(BaseModel):
    query: str


@router.post("")
def chat(request: ChatRequest):

   answer = ask_agent(request.query)
   print(request.query,answer);
   return {
        "success": True,
        "answer": answer
    }