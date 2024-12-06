from fastapi import APIRouter, Request, Response
from app.schemas.misc_schemas import HealthcheckSchema
from app.config import settings

router = APIRouter()


@router.get("/helthcheck", response_model=HealthcheckSchema)
def healthcheck(request: Request):
    return HealthcheckSchema(status="OK", version=settings.app.app_version)
