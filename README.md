# URL Shortener Service

## Features
- **URL Shortening**: Generates a unique short code for a given long URL.
- **Redirection**: Redirects from the short link to the original URL.
- **Click Tracking**: Logs metrics on how many times a short link has been accessed.
- **API Docs**: Interactive Swagger documentation available at `/docs`.

## Project Architecture
- `models/`: Database schemas (SQLAlchemy ORM)
- `schemas/`: Data validation and serialization (Pydantic)
- `services/`: Core business logic (short code generation, DB operations)
- `routers/`: API endpoints and HTTP response mapping
- `database.py`: Database connection setup and session lifecycle

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/shorten` | Submits a long URL and returns the generated short code. |
| `GET` | `/{short_code}` | Redirects to the original URL and increments the click counter. |
| `GET` | `/stats/{short_code}` | Returns analytics (creation date, click counts) for the short code. |

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/url-shortener.git](https://github.com/YOUR_GITHUB_USERNAME/url-shortener.git)
   cd url-shortener

Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the server:
uvicorn app.main:app --reload

Open http://127.0.0.1:8000/docs in your browser to test the API.