from bluehealth.services import (
    create_user,
    get_all_patients_pagination,
    get_all_pharmacies_pagination,
    get_all_transactions_pagination,
)


def test_create_user():
    username = 'teste'
    user = create_user(username, '123')
    assert user.username == username


def test_get_all_patients_pagination(patient1, patient2):
    pagination = get_all_patients_pagination(
        1, 10, first_name=patient1.first_name, last_name=patient1.last_name
    )
    assert pagination.total == 1


def test_get_all_pharmacies_pagination(pharmacy1, pharmacy2):
    pagination = get_all_pharmacies_pagination(
        1, 10, name=pharmacy1.name, city=pharmacy1.city
    )
    assert pagination.total == 1


def test_get_all_transactions_pagination(transaction1, transaction2):
    pagination = get_all_transactions_pagination(
        1,
        10,
        patient_first_name=transaction1.patient.first_name,
        patient_last_name=transaction1.patient.last_name,
    )
    assert pagination.total == 1
