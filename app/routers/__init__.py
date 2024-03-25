from fastapi import APIRouter

from app.routers import admin, answer, participant, question, result, welcome

api_router = APIRouter()
api_router.include_router(welcome.router, prefix="", tags=["Welcome"])
api_router.include_router(participant.router, prefix="/participants", tags=["Participant"])
api_router.include_router(question.router, prefix="/questions", tags=["Question"])
api_router.include_router(answer.router, prefix="/answers", tags=["Answer"])
api_router.include_router(result.router, prefix="/results", tags=["Result"])
api_router.include_router(admin.router, prefix="/admin", tags=["Admin"])
