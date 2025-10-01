from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    value: Optional[float] = None
    # created_at: datetime # this is auto set by the database
    scheduled_to: datetime
    executed_at: Optional[datetime] = None


class TaskRead(BaseModel):
    id: int
    name: str
    value: Optional[float] = None
    created_at: datetime
    scheduled_to: datetime
    executed_at: Optional[datetime] = None
