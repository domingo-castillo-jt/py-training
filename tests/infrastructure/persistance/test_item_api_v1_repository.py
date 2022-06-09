from src.core.domain.entities.item import ItemFactory
from src.infrastructure.persistance.item_api_v1_repository import ItemApiV1Repository

def test_get_all_returns_item_list(requests_mock):
    item_quantity = 4
    item_list = [ItemFactory.build(id = x) for x in range(item_quantity)]
    response_mock = { "result": { "items": [dict(item) for item in item_list]}}
    requests_mock.get(f"http://api.rollbar.com/api/1/items", json=response_mock)
    item_response =ItemApiV1Repository().get_all()
    assert(len(item_response) == item_quantity)
    for index, item in enumerate(item_response):
        print("HOLAAA")
        assert(item.id == index)

def test_get_one_returns_one_item(requests_mock):
    id = 1
    item_fixture = ItemFactory.build(id = id)
    response_mock = { "result": dict(item_fixture)}
    requests_mock.get(f"http://api.rollbar.com/api/1/item/{id}", json=response_mock)
    assert(ItemApiV1Repository().get_one(id).id == id)
    assert(ItemApiV1Repository().get_one(id) == item_fixture)

