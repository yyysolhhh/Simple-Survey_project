from fastapi import HTTPException

from database_settings import SessionLocal, AsyncSessionLocal


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session


def response(data):
    if data is None:
        raise HTTPException(status_code=404, detail=f"{data} Not Found")
    return data
