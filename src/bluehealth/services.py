from flask_sqlalchemy.pagination import SelectPagination
from werkzeug.security import generate_password_hash

from bluehealth.database import db
from bluehealth.models import Patient, Pharmacy, Transaction, User


def get_all_patients_pagination(
    page: int, per_page: int, first_name: str = None, last_name: str = None
) -> SelectPagination:
    """
    Get all patients and put in a SelectPagination object.
    """
    result = db.select(Patient)
    if first_name:
        result = result.filter(Patient.first_name.ilike(f'%{first_name}%'))
    if last_name:
        result = result.filter(Patient.last_name.ilike(f'%{last_name}%'))
    pagination = db.paginate(result, page=page, per_page=per_page)
    return pagination


def get_all_pharmacies_pagination(
    page: int, per_page: int, name: str = None, city: str = None
) -> SelectPagination:
    """
    Get all pharmacy and put in a SelectPagination object.
    """
    result = db.select(Pharmacy)
    if name:
        result = result.filter(Pharmacy.name.ilike(f'%{name}%'))
    if city:
        result = result.filter(Pharmacy.city.ilike(f'%{city}%'))
    pagination = db.paginate(result, page=page, per_page=per_page)
    return pagination


def get_all_transactions_pagination(
    page: int,
    per_page: int,
    patient_first_name: str = None,
    patient_last_name: str = None,
) -> SelectPagination:
    """
    Get all transaction and put in a SelectPagination object.
    """
    result = db.select(Transaction).join(Patient)
    if patient_first_name:
        result = result.filter(
            Patient.first_name.ilike(f'%{patient_first_name}%')
        )
    if patient_last_name:
        result = result.filter(
            Patient.last_name.ilike(f'%{patient_last_name}%')
        )
    pagination = db.paginate(result, page=page, per_page=per_page)
    return pagination


def create_user(username: str, password: str) -> User:
    """
    Create a new user with username and password.
    """
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return user
