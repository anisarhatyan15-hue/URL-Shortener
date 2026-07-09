from datetime import datetime
from pydantic import BaseModel, HttpUrl

class URLCreateRequest(BaseModel):
    original_url: HttpUrl

class URLResponse(BaseModel):
    id: int
    original_url: HttpUrl
    short_code: str
    click_count: int
    created_at: datetime

class Config:
   from_attributes = True   
