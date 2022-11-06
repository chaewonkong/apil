from fastapi.routing import APIRouter

refugee_controller = APIRouter()

@refugee_controller.get("/", name="난민 정보 조회")
async def find_refugees():
    return ""