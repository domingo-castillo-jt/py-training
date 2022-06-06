from pydantic import BaseModel
from typing import Union

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
    last_muted_timestamp: Union[int,None]
    last_occurrence_id: int
    last_occurrence_timestamp: int
    total_occurrences: int
    last_modified_by: int
    status: str
    level: str
    integrations_data: Union[int,None]
    assigned_user_id: Union[int,None]
    group_item_id: Union[int,None]
    group_status: int
