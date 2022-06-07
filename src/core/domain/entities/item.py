from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id: int
    project_id: int
    counter: int
    environment: str
    platform: str
    framework: str
    hash: str
    title: str
    first_occurrence_id: int
    first_occurrence_timestamp: int
    activating_occurrence_id: int
    last_activated_timestamp: int
    last_resolved_timestamp: int
    last_muted_timestamp: Optional[int]
    last_occurrence_id: int
    last_occurrence_timestamp: int
    total_occurrences: int
    last_modified_by: int
    status: str
    level: str
    integrations_data: Optional[int]
    assigned_user_id: Optional[int]
    group_item_id: Optional[int]
    group_status: int
