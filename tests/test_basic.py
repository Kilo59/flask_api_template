"""Basic Tests"""


def test_index(api_client):
    with api_client as client:
        assert b"Hello World!" == client.get("/").data


def test_status(api_client):
    with api_client as client:
        assert 200 == client.get("/status").status_code
