from bluehealth.models import User


def test_list_patients_status_200(client):
    response = client.get('/patients/')
    assert response.status_code == 200


def test_list_pacients_status_unauthorized(client):
    response = client.get(
        '/patients/', headers={'Authorization': 'Basic errado'}
    )
    assert response.status_code == 401


def test_list_pharmacies_status_200(client):
    response = client.get('/pharmacies/')
    assert response.status_code == 200


def test_list_transactions_status_200(client):
    response = client.get('/transactions/')
    assert response.status_code == 200
