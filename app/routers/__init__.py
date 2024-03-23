from fastapi import APIRouter

from app.routers import answer, participant, question, welcome, result

# from fastapi.templating import Jinja2Templates
#
# templates = Jinja2Templates(directory="app/templates")
api_router = APIRouter()


api_router.include_router(welcome.router, prefix="")
api_router.include_router(participant.router, prefix="/participants")
api_router.include_router(question.router, prefix="/questions")
api_router.include_router(answer.router, prefix="/answers")
api_router.include_router(result.router, prefix="/results")
