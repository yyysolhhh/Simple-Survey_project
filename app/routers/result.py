from typing import Any

from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.responses import JSONResponse

from app.routers.welcome import templates
from app.services.result import get_result_graphs

router = APIRouter()


@router.get("", response_class=HTMLResponse)
async def show_results() -> Any:
    graphs_json = get_result_graphs()
    return templates.TemplateResponse("results.html", context={"graphs_json": graphs_json})
