from typing import Any

from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from app.services.result import get_result_graphs


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
async def show_results(request: Request) -> Any:
    graphs_json = await get_result_graphs()
    return templates.TemplateResponse(request=request, name="results.html", context={"graphs_json": graphs_json})
