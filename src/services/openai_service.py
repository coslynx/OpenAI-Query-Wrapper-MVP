from typing import Optional
import openai
from src.config.config import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

class OpenAIService:
    """
    Provides a service layer for interacting with the OpenAI API.

    Handles sending requests, processing responses, and managing potential errors.
    """

    @classmethod
    async def initialize(cls):
        """
        Initializes the OpenAI service.

        Sets up the OpenAI client and any necessary configurations.
        """
        openai.api_key = settings.OPENAI_API_KEY  # Load API key from environment variables

    @classmethod
    async def shutdown(cls):
        """
        Shuts down the OpenAI service.

        Cleans up any resources or connections.
        """
        pass  # Add any cleanup logic if needed

    @classmethod
    async def generate_response(cls, model: str, prompt: str, 
                               temperature: Optional[float] = 0.7, 
                               max_tokens: Optional[int] = 2048,
                               top_p: Optional[float] = 1.0,
                               frequency_penalty: Optional[float] = 0.0,
                               presence_penalty: Optional[float] = 0.0) -> dict:
        """
        Generates a response from the OpenAI API.

        Args:
            model: The name of the OpenAI model to use (e.g., "text-davinci-003").
            prompt: The user's input for the AI model to process.
            temperature: Controls the creativity of the output (default: 0.7).
            max_tokens: Limits the output length (default: 2048).
            top_p: Controls the randomness of the output (default: 1.0).
            frequency_penalty: Penalty for repeating words (default: 0.0).
            presence_penalty: Penalty for including specific words (default: 0.0).

        Returns:
            A dictionary containing the generated text and relevant metadata.

        Raises:
            openai.error.APIError: If the OpenAI API call fails.
            Exception: If an unexpected error occurs.
        """
        try:
            logger.info(f"Sending OpenAI request: model={model}, prompt={prompt}, temperature={temperature}, max_tokens={max_tokens}, top_p={top_p}, frequency_penalty={frequency_penalty}, presence_penalty={presence_penalty}")
            response = await openai.Completion.create(
                model=model,
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty
            )
            logger.info(f"Received OpenAI response: {response}")
            return response.to_dict()
        except openai.error.APIError as e:
            logger.error(f"OpenAI API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during OpenAI request: {e}")
            raise