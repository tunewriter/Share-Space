from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
test_key = '1234'
test_boardname = 'Number Cave'


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"page": "Home Page"}


def test_save_note():
    response = client.post(
        "http:///addnote/",
        json={'cave_key': test_key,
              'data': 'PyTest_data'}
    )
    assert response.status_code == 200
    assert response.json() == {
        'cave_key': '1234',
        'data': 'PyTest_data'
    }


def test_get_notes():
    response = client.get(f"/notes/{test_key}")
    assert response.status_code == 200
    assert len(response.json()[0]) >= 5  # more than 5 elements


def test_check_key():
    response = client.get(f"/check/{test_key}")
    assert response.status_code == 200
    assert response.json() == {'state': 'true',
                                'name': test_boardname}
