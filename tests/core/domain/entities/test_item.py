from pydantic import ValidationError
from src.core.domain.entities.item import Item

try:
    item = Item(id="casa")
    assert False
except ValidationError:
    assert True

item = Item(
id= 1263994911,
project_id= 569699,
counter= 2,
environment= "production",
platform= "unknown",
framework= "flask",
hash= "b17ef14f24adcf72f534c4e596032ad3452b162a",
title= "TypeError: The view function did not return a valid response. The return type must be a string, dict, tuple,Response instance, or WSGI callable, but it was a Response.",
first_occurrence_id= 232638159006,
first_occurrence_timestamp= 1654243013,
activating_occurrence_id= 232638159006,
last_activated_timestamp= 1654243013,
last_resolved_timestamp= 1654497394,
last_muted_timestamp= None,
last_occurrence_id= 232640892231,
last_occurrence_timestamp= 1654244517,
total_occurrences= 2,
last_modified_by= 1062,
status= "resolved",
level= "error",
integrations_data= None,
assigned_user_id= None,
group_item_id= None,
group_status= 1)

assert item.id == 1263994911
