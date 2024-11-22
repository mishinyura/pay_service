from typing import Literal

from pydantic import BaseModel

class HealthcheckSchema(BaseModel):
    status: str
    version: str