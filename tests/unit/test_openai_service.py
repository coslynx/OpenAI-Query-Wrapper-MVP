import pytest
from unittest.mock import patch
from src.services.openai_service import OpenAIService
from src.config.config import settings

@pytest.fixture
def openai_service():
    return OpenAIService

@patch('openai.Completion.create')
async def test_generate_response(mock_completion_create, openai_service):
    model = "text-davinci-003"
    prompt = "Write a short story about a cat"
    temperature = 0.7
    max_tokens = 2048
    top_p = 1.0
    frequency_penalty = 0.0
    presence_penalty = 0.0

    mock_completion_create.return_value = {
        "choices": [
            {
                "text": "Once upon a time, there was a cat named Whiskers...",
                "index": 0,
                "logprobs": None,
                "finish_reason": "length"
            }
        ]
    }

    response = await openai_service.generate_response(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    assert response["choices"][0]["text"] == "Once upon a time, there was a cat named Whiskers..."
    mock_completion_create.assert_called_once_with(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

@patch('openai.Completion.create')
async def test_generate_response_api_error(mock_completion_create, openai_service):
    mock_completion_create.side_effect = openai.error.APIError("API error")
    model = "text-davinci-003"
    prompt = "Write a short story about a cat"

    with pytest.raises(openai.error.APIError):
        await openai_service.generate_response(model=model, prompt=prompt)

    mock_completion_create.assert_called_once_with(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

@patch('openai.Completion.create')
async def test_generate_response_unexpected_error(mock_completion_create, openai_service):
    mock_completion_create.side_effect = Exception("Unexpected error")
    model = "text-davinci-003"
    prompt = "Write a short story about a cat"

    with pytest.raises(Exception):
        await openai_service.generate_response(model=model, prompt=prompt)

    mock_completion_create.assert_called_once_with(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

@patch('openai.api_key', settings.OPENAI_API_KEY)
async def test_initialize(openai_service):
    await openai_service.initialize()
    assert openai.api_key == settings.OPENAI_API_KEY