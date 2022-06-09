from typing import Optional

from pydantic import BaseModel
from pydantic_factories import ModelFactory


class Item(BaseModel):
    id: Optional[int]
    project_id: Optional[int]
    counter: Optional[int]
    environment: Optional[str]
    platform: Optional[str]
    framework: Optional[str]
    hash: Optional[str]
    title: Optional[str]
    first_occurrence_id: Optional[int]
    first_occurrence_timestamp: Optional[int]
    activating_occurrence_id: Optional[int]
    last_activated_timestamp: Optional[int]
    last_resolved_timestamp: Optional[int]
    last_muted_timestamp: Optional[int]
    last_occurrence_id: Optional[int]
    last_occurrence_timestamp: Optional[int]
    total_occurrences: Optional[int]
    last_modified_by: Optional[int]
    status: Optional[str]
    level: Optional[str]
    integrations_data: Optional[int]
    assigned_user_id: Optional[int]
    group_item_id: Optional[int]
    group_status: Optional[int]

