from datetime import datetime

import pytest
from flask import testing
from werkzeug.datastructures import Headers
from werkzeug.security import generate_password_hash

from bluehealth.app import create_app
from bluehealth.database import db
from bluehealth.models import Patient, Pharmacy, Transaction, User


@pytest.fixture(autouse=True)
def app():
    flask_app = create_app('testing')
    flask_app.app_context().push()
    db.create_all()
    yield flask_app


class TestClient(testing.FlaskClient):
    def open(self, *args, **kwargs):
        headers = kwargs.pop('headers', Headers())
        if not headers.get('Authorization'):
            headers.update(
                {'Authorization': 'Basic dGVzdGU6MTIz'}
            )   # base64('teste:123')
        kwargs['headers'] = headers
        return super().open(*args, **kwargs)


@pytest.fixture
def user():
    user = User(username='teste', password=generate_password_hash('123'))
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def client(app, user):
    app.test_client_class = TestClient
    return app.test_client()


@pytest.fixture
def patient1():
    patient = Patient(
        uuid='PATIENT0001',
        first_name='John',
        last_name='Doe',
        date_of_birth=datetime(1990, 1, 1),
    )
    db.session.add(patient)
    db.session.commit()
    return patient


@pytest.fixture
def patient2():
    patient = Patient(
        uuid='PATIENT0002',
        first_name='Jane',
        last_name='Doe',
        date_of_birth=datetime(1991, 1, 1),
    )
    db.session.add(patient)
    db.session.commit()
    return patient


@pytest.fixture
def pharmacy1():
    pharmacy = Pharmacy(
        uuid='PHARMACY0001',
        name='Pharmacy 1',
        city='City 1',
    )
    db.session.add(pharmacy)
    db.session.commit()
    return pharmacy


@pytest.fixture
def pharmacy2():
    pharmacy = Pharmacy(
        uuid='PHARMACY0002',
        name='Pharmacy 2',
        city='City 2',
    )
    db.session.add(pharmacy)
    db.session.commit()
    return pharmacy


@pytest.fixture
def transaction1(patient1, pharmacy1):
    transaction = Transaction(
        uuid='TRANSACTION0001',
        patient_uuid=patient1.uuid,
        pharmacy_uuid=pharmacy1.uuid,
        amount=100,
        timestamp=datetime.now(),
    )
    db.session.add(transaction)
    db.session.commit()
    return transaction


@pytest.fixture
def transaction2(patient2, pharmacy2):
    transaction = Transaction(
        uuid='TRANSACTION0002',
        patient_uuid=patient2.uuid,
        pharmacy_uuid=pharmacy2.uuid,
        amount=200,
        timestamp=datetime.now(),
    )
    db.session.add(transaction)
    db.session.commit()
    return transaction
