import pytest
from task1 import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_equipment(client):
    response = client.get('/api/equipment')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 5
    assert data[0]['id'] == 101
    assert data[0]['name'] == 'flight control unit'
    assert data[0]['type'] == 'FCU'
    assert data[0]['status'] == 'operational'
    assert data[1]['id'] == 102
    assert data[1]['name'] == 'navigation system'
    assert data[1]['type'] == 'NS'
    assert data[1]['status'] == 'operational'

@pytest.mark.parametrize("equipment_id", [101])
def test_get_equipment_by_id(client, equipment_id):
    response = client.get(f'/api/equipment/{equipment_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == equipment_id
    assert data['name'] == 'flight control unit'
    assert data['type'] == 'FCU'
    assert data['status'] == 'operational'