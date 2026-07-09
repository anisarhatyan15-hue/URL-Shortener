import random 
import string

from sqlalchemy.orm import Session

from app.models.url import URL

CODE_LENGTH = 6
CHARACTERS = string.ascii_letters + string.digits

def generate_short_code() -> str:
   return "".join(random.choices(CHARACTERS, k=CODE_LENGTH))

def create_unique_short_code(db: Session) -> str:
   while True:
        code = generate_short_code()
        existing = db.query(URL).filter(URL.short_code == code).first()
        if not existing:
            return code
        
def create_short_url(db: Session, original_url: str) -> URL:
    short_code = create_unique_short_code(db)

    new_url = URL(
        original_url=original_url,
        short_code=short_code,
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url

def get_url_by_code(db: Session, short_code: str) -> URL | None:
    return db.query(URL).filter(URL.short_code == short_code).first()

def increment_click_count(db: Session, url_entry: URL) -> URL:
    url_entry.click_count += 1
    db.commit()
    db.refresh(url_entry)
    return url_entry