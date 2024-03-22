from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse

from routers.welcome import templates
# import templates
# from fastapi.templating import Jinja2Templates
#
# templates = Jinja2Templates(directory="app/templates")

router = APIRouter()


@router.get("", response_class=HTMLResponse)
async def participant(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="participant.html")
