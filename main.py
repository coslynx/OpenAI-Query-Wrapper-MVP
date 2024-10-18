from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from src.services.openai_service import OpenAIService
from src.config.config import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the application...")
    await OpenAIService.initialize()
    logger.info("Application started successfully.")

@app.post("/v1/query/")
async def query_openai(request: Request, model: str = Form(...), prompt: str = Form(...), 
                      temperature: Optional[float] = Form(0.7), 
                      max_tokens: Optional[int] = Form(2048), 
                      top_p: Optional[float] = Form(1.0), 
                      frequency_penalty: Optional[float] = Form(0.0), 
                      presence_penalty: Optional[float] = Form(0.0)):
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
        return JSONResponse({"error": str(e)}, status_code=500)

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the application...")
    await OpenAIService.shutdown()
    logger.info("Application shut down successfully.")