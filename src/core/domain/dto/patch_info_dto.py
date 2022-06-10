from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConstrainedStr, validator


class StatusEnum(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    MUTED = "muted"


class LevelEnum(str, Enum):
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"


class ConstrMax40(ConstrainedStr):
    max_length = 40


class ConstrMax255Min1(ConstrainedStr):
    max_length = 255
    min_length = 1


class PatchInfo(BaseModel):
    status: Optional[StatusEnum]
    resolved_in_version: Optional[ConstrMax40]  # if status = resolved
    title: Optional[ConstrMax255Min1]
    level: Optional[LevelEnum]
    assigned_user_id: Optional[int]
    @validator('resolved_in_version')
    def optional_if_status(cls, v, values, **kwargs):
        if 'status' in values and values['status'] != "resolved" and v is not None:
            raise ValueError("Should be empty if status not 'resolved'")



