from fastapi.routing import APIRouter
from app.controller import refugee_controller

router = APIRouter()

@router.get("/")
def healthCheck() -> str:
    return "ok"


router.include_router(refugee_controller, prefix="/refugees", tags=["refugee"])