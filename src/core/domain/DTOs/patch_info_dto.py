from enum import Enum
from typing import Optional

from pydantic import BaseModel, constr


class status_enum(str, Enum):
    active = "active"
    resolved = "resolved"
    muted = "muted"


class level_enum(str, Enum):
    critical = "critical"
    error = "error"
    warning = "warning"
    info = "info"
    debug = "debug"


class PatchInfo(BaseModel):
    status: Optional[status_enum]
    resolved_in_version: Optional[constr(max_length=40)]  # if status = resolved
    title: Optional[constr(min_length=1, max_length=255)]
    level: Optional[level_enum]
    assigned_user_id: Optional[int]
