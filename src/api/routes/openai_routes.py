from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from typing import Optional
from src.services.openai_service import OpenAIService
from src.config.config import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/v1", tags=["OpenAI"])

@router.post("/query/")
async def query_openai(request: Request, model: str = Form(...), prompt: str = Form(...), 
                      temperature: Optional[float] = Form(0.7), 
                      max_tokens: Optional[int] = Form(2048), 
                      top_p: Optional[float] = Form(1.0), 
                      frequency_penalty: Optional[float] = Form(0.0), 
                      presence_penalty: Optional[float] = Form(0.0)):
    """
    Handles user requests for generating AI responses using OpenAI API.
    """
    try:
        logger.info(f"Received request: model={model}, prompt={prompt}, temperature={temperature}, max_tokens={max_tokens}, top_p={top_p}, frequency_penalty={frequency_penalty}, presence_penalty={presence_penalty}")
        response = await OpenAIService.generate_response(model=model, prompt=prompt, 
                                                    temperature=temperature, 
                                                    max_tokens=max_tokens, 
                                                    top_p=top_p, 
                                                    frequency_penalty=frequency_penalty, 
                                                    presence_penalty=presence_penalty)
        logger.info(f"Response generated successfully: {response}")
        return JSONResponse(response)
    except Exception as e:
        logger.error(f"Error processing OpenAI request: {e}")
        return JSONResponse({ "error": str(e) }, status_code=500)