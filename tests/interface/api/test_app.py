from src.interface.api.app import app

def test_hello() -> None:
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"
