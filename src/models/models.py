from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.config.config import settings
from src.utils.logger import get_logger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

logger = get_logger(__name__)

Base = declarative_base()

class OpenAIRequest(Base):
    __tablename__ = "openai_requests"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)
    prompt = Column(String, nullable=False)
    temperature = Column(Float, nullable=False, default=0.7)
    max_tokens = Column(Integer, nullable=False, default=2048)
    top_p = Column(Float, nullable=False, default=1.0)
    frequency_penalty = Column(Float, nullable=False, default=0.0)
    presence_penalty = Column(Float, nullable=False, default=0.0)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="openai_requests")

    def __repr__(self):
        return f"<OpenAIRequest id={self.id}, model={self.model}, prompt={self.prompt}>"

class OpenAIResponse(Base):
    __tablename__ = "openai_responses"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("openai_requests.id"), nullable=False)
    response_text = Column(String, nullable=False)
    response_json = Column(String, nullable=True)  # Store response as JSON
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    request = relationship("OpenAIRequest", back_populates="responses")

    def __repr__(self):
        return f"<OpenAIResponse id={self.id}, request_id={self.request_id}, response_text={self.response_text[:20]}>"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    api_key = Column(String, nullable=False)  # Store API key securely
    openai_requests = relationship("OpenAIRequest", back_populates="user")

    def __repr__(self):
        return f"<User id={self.id}, username={self.username}>"