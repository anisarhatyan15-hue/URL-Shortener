from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from app.database import get_db
from app.schemas.url import URLCreateRequest, URLResponse
from app.services import url_service


router = APIRouter()
@router.post("/shorten", response_model=URLResponse)
def shorten_url(request: URLCreateRequest, db: Session = Depends(get_db)):
    new_url = url_service.create_short_url(db, str(request.original_url))
    return new_url

@router.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
        url_entry = url_service.get_url_by_code(db, short_code)

        if not url_entry:
            raise HTTPException(status_code=404, detail="Short URL not found")

        url_service.increment_click_count(db, url_entry)

        return RedirectResponse(url=str(url_entry.original_url))

@router.get("/stats/{short_code}", response_model=URLResponse)
def get_stats(short_code: str, db: Session = Depends(get_db)):
     url_entry = url_service.get_url_by_code(db, short_code)

     if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")

     return url_entry