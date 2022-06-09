from enum import Enum
from typing import Optional

from pydantic import BaseModel, constr
from pydantic_factories import ModelFactory


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


class PatchInfo(BaseModel):
    status: Optional[StatusEnum]
    resolved_in_version: Optional[constr(max_length=40)]  # if status = resolved
    title: Optional[constr(min_length=1, max_length=255)]
    level: Optional[LevelEnum]
    assigned_user_id: Optional[int]


class PatchInfoFactory(ModelFactory):
    __model__ = PatchInfo
