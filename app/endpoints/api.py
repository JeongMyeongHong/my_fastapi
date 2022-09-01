from fastapi import APIRouter

import login, users, detectors

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(detectors.router, prefix="/detectors", tags=["detectors"])