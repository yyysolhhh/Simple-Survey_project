from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse

from routers.welcome import templates
from services.participant import get_participant
from dtos.participant import ParticipantResponse

from models.participant import Participant

# import templates
# from fastapi.templating import Jinja2Templates
#
# templates = Jinja2Templates(directory="app/templates")

router = APIRouter()


@router.get("", response_class=HTMLResponse)
def get_form(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="participant.html")


@router.post("")
async def submit_form(data: ParticipantResponse):
    await get_participant(name=data.name, age=data.age, gender=data.gender)
    return {"redirect": "/questions", "participant_id": 1}  # debug url_for


# @router.post("")
# # def submit_form(name: Annotated[str, Form()], age: Annotated[int, Form()], gender: Annotated[str, Form()]):
# def submit_form(name: str = Form(...), age: int = Form(...), gender: str = Form(...)):
#     participant = {"name": name, "age": age, "gender": gender}
#     print(name, age, gender)
#     # get_participant(name=name, age=age, gender=gender)
#     return RedirectResponse(url="/questions", status_code=302)
#     # return participant


# @router.post("")
# async def submit_form(request: Request):
#     data = await request.body()
#     participant = Participant(name=data.name, age=data.age, gender=data.gender)
#     print(participant)
#     # return RedirectResponse(url="/participant", status_code=202)
#     # return JSONResponse(participant)
#     return {"redirect": "/questions", "participant_id": 1}