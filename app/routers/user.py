from fastapi import APIRouter, Body

from app.schemas import CreateUser, UpdateUser

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/")
async def all_users():
    pass

@router.get("/{user_id}")
async def user_by_id(user_id: int):
    pass

@router.post("/create")
async def create_user(user: CreateUser = Body(...)):
    pass

@router.put("/update")
async def update_user(user: UpdateUser = Body(...)):
    pass

@router.delete("/delete")
async def delete_user(user_id: int):
    pass