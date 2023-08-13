from fastapi import Request, Form, APIRouter, Cookie, Query, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="template")

# Route for the shop selection page
@router.get("/store", response_class=HTMLResponse)
async def get_main_page(request :Request):

    user_id = request.session.get("user_id")
    firstname = request.session.get("firstname")
    lastname = request.session.get("lastname")
    isShop = request.session.get("isShop")
    shop_id = request.session.get("shop_id")

    return templates.TemplateResponse("store.html", {"request": request, "user_id": user_id, "firstname": firstname, "lastname": lastname, "isShop": isShop, "shop_id": shop_id})

