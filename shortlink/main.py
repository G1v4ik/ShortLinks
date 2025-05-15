import validators

from starlette.datastructures import URL

from fastapi.responses import JSONResponse

from fastapi import (
    Depends,
    FastAPI,
    Request,
    Response,
    HTTPException
)

from sqlalchemy.orm import Session

from . import schemas, models, crud
from .database import SessionLocal, engine
from .config import get_settings

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    
    finally:
        db.close()


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

def raise_not_found(request):
    messsage = f"URL '{request.url}' doesn`t exist"
    raise HTTPException(status_code=404, detail=messsage)


@app.post('/url', response_model=schemas.URL)
def create_url(url: schemas.URLBase, db:Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
    
    db_url = crud.create_db_url(db=db, url=url)
    info = get_url_info(db_url)
    return JSONResponse(content={
        "target_url": info.target_url,
        "url": info.url,
        "key": info.key
        }, status_code=201)


@app.get('/{url_key}', response_model=schemas.URL)
def forward_to_target_url(
    url_key: str,
    request: Request,
    db: Session = Depends(get_db)
):
    if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
        return Response(None, headers={"target_url": db_url.target_url}, status_code=307)
    
    else:
        raise_not_found(request)


def get_url_info(db_url: models.URL) -> schemas.URL:
    base_url = URL(get_settings().base_url)
    db_url.url = str(base_url.replace(path=db_url.key))
    return db_url