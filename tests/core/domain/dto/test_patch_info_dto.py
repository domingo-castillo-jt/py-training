from pydantic import ValidationError
import pytest
from src.core.domain.dto.patch_info_dto import PatchInfo


def test_create_data_info_if_correct_data():
    PatchInfo(status= "resolved", resolved_in_version= "aabbcc1", title= "test tile 134")

def test_raise_error_if_resolved_in_version_but_not_resolved():
    with pytest.raises(ValidationError):
        PatchInfo(status= "active", resolved_in_version= "aabbcc1", title= "test tile 134")
