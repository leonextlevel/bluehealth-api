from apiflask import APIBlueprint, pagination_builder

from bluehealth.authentication import auth
from bluehealth.schemas import (
    PaginationQuery,
    PatientFilter,
    PatientPaginationOut,
    PharmacyFilter,
    PharmacyPaginationOut,
    TransactionFilter,
    TransactionPaginationOut,
)
from bluehealth.services import (
    get_all_patients_pagination,
    get_all_pharmacies_pagination,
    get_all_transactions_pagination,
)

patients_bp = APIBlueprint('patients', __name__, tag='Patients')
pharmacies_bp = APIBlueprint('pharmacies', __name__, tag='Pharmacies')
transactions_bp = APIBlueprint('transactions', __name__, tag='Transactions')


@patients_bp.get('/patients/')
@patients_bp.input(PaginationQuery, location='query', arg_name='pagination')
@patients_bp.input(PatientFilter, location='query', arg_name='filter')
@patients_bp.output(PatientPaginationOut)
@patients_bp.auth_required(auth)
def list_patients_with_pagination(pagination: dict, filter: dict) -> dict:
    """List all patients with pagination."""
    pagination = get_all_patients_pagination(**pagination, **filter)
    return {
        'results': pagination.items,
        'pagination': pagination_builder(pagination),
    }


@pharmacies_bp.get('/pharmacies/')
@pharmacies_bp.input(PaginationQuery, location='query', arg_name='pagination')
@pharmacies_bp.input(PharmacyFilter, location='query', arg_name='filter')
@pharmacies_bp.output(PharmacyPaginationOut)
@pharmacies_bp.auth_required(auth)
def list_pharmacies_with_pagination(pagination: dict, filter: dict) -> dict:
    """List all pharmacies with pagination."""
    pagination = get_all_pharmacies_pagination(**pagination, **filter)
    return {
        'results': pagination.items,
        'pagination': pagination_builder(pagination),
    }


@transactions_bp.get('/transactions/')
@transactions_bp.input(
    PaginationQuery, location='query', arg_name='pagination'
)
@transactions_bp.input(TransactionFilter, location='query', arg_name='filter')
@transactions_bp.output(TransactionPaginationOut)
@transactions_bp.auth_required(auth)
def list_transactions_with_pagination(pagination: dict, filter: dict) -> dict:
    """List all transactions with pagination."""
    pagination = get_all_transactions_pagination(**pagination, **filter)
    return {
        'results': pagination.items,
        'pagination': pagination_builder(pagination),
    }
