from typing import Annotated, Any

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from tortoise.backends.base.client import BaseDBAsyncClient
from werkzeug.security import check_password_hash

from app.configs.constants import TEMPLATES
from app.configs.database_settings import connect_db
from app.dtos.admin import AdminInDB
from app.models.admin import Admin
from app.services.admin import create_new_admin
from app.services.answer import collect_answers

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES)


@router.get("/signup")
def get_signup_page(request: Request) -> Any:
    return templates.TemplateResponse(request=request, name="signup.html")


@router.post("/signup")
async def signup(new_admin: AdminInDB, conn: BaseDBAsyncClient = Depends(connect_db)) -> None:
    # admin = Admin.get_admin(new_admin.username)
    # print(admin.username)
    # if admin:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Admin User already exists")
    await create_new_admin(new_admin, conn)


@router.get("/login")
def get_login_page(request: Request) -> Any:
    return templates.TemplateResponse(request=request, name="admin.html")


# @router.post("/login")
# def login(request: Request, login_form: OAuth2PasswordRequestForm = Depends(), username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     admin = Admin.get_admin(username)


@router.get("/dashboard", response_class=HTMLResponse)
def get_dashboard_page(request: Request) -> None:
    pass
    # graph_div =
    # return templates.TemplateResponse(request=request, name="dashboard.html", context={"graph_div": graph_div})
